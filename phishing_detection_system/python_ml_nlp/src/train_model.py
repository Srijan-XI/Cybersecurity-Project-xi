#!/usr/bin/env python3
"""
Model Training Script for Phishing URL Detection
Author: Cybersecurity Project XI
Date: September 2025

This script trains multiple machine learning models on phishing detection datasets
and saves the best performing model for deployment.
"""

import os
import sys
import pandas as pd
import numpy as np
import pickle
import joblib
from datetime import datetime
from typing import Dict, List, Tuple, Any

# Scikit-learn imports
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report
)
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest, f_classif

# Import our NLP processing module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from nlp_processing import URLFeatureExtractor, preprocess_dataset

class PhishingModelTrainer:
    """
    Comprehensive phishing detection model trainer
    """
    
    def __init__(self, data_dir: str = '../data', models_dir: str = '../models'):
        self.data_dir = data_dir
        self.models_dir = models_dir
        self.models = {}
        self.best_model = None
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        self.feature_selector = SelectKBest(f_classif, k=30)
        
        # Ensure models directory exists
        os.makedirs(models_dir, exist_ok=True)
    
    def load_datasets(self) -> pd.DataFrame:
        """
        Load and combine all available datasets
        """
        print("📊 Loading datasets...")
        
        datasets = []
        
        # Load dataset_phishing.csv
        try:
            df1 = pd.read_csv(os.path.join(self.data_dir, 'dataset_phishing.csv'))
            if 'status' in df1.columns:
                df1['label'] = df1['status'].map({'legitimate': 0, 'phishing': 1})
                datasets.append(df1.drop('status', axis=1))
                print(f"  ✅ Loaded dataset_phishing.csv: {len(df1)} samples")
        except Exception as e:
            print(f"  ❌ Error loading dataset_phishing.csv: {e}")
        
        # Load Phishing_Legitimate_full.csv
        try:
            df2 = pd.read_csv(os.path.join(self.data_dir, 'Phishing_Legitimate_full.csv'))
            if 'CLASS_LABEL' in df2.columns:
                df2['label'] = df2['CLASS_LABEL']
                datasets.append(df2.drop('CLASS_LABEL', axis=1))
                print(f"  ✅ Loaded Phishing_Legitimate_full.csv: {len(df2)} samples")
        except Exception as e:
            print(f"  ❌ Error loading Phishing_Legitimate_full.csv: {e}")
        
        if not datasets:
            raise ValueError("No datasets could be loaded!")
        
        # Combine datasets
        combined_df = pd.concat(datasets, ignore_index=True, sort=False)
        
        # Handle missing values
        combined_df = combined_df.fillna(0)
        
        print(f"📈 Combined dataset: {len(combined_df)} samples")
        print(f"📋 Features: {len(combined_df.columns) - 1}")
        
        # Print label distribution
        if 'label' in combined_df.columns:
            label_counts = combined_df['label'].value_counts()
            print(f"📊 Label distribution:")
            print(f"  - Legitimate (0): {label_counts.get(0, 0)}")
            print(f"  - Phishing (1): {label_counts.get(1, 0)}")
        
        return combined_df
    
    def prepare_features(self, df: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray, List[str]]:
        """
        Prepare features and target variables
        """
        print("🔧 Preparing features...")
        
        # Separate features and target
        if 'label' not in df.columns:
            raise ValueError("No 'label' column found in dataset!")
        
        # Remove non-feature columns
        feature_columns = [col for col in df.columns 
                          if col not in ['label', 'url', 'id', 'CLASS_LABEL', 'status']]
        
        X = df[feature_columns].values
        y = df['label'].values
        
        # Handle categorical target if needed
        if y.dtype == 'object':
            y = self.label_encoder.fit_transform(y)
        
        print(f"  ✅ Feature matrix shape: {X.shape}")
        print(f"  ✅ Target vector shape: {y.shape}")
        
        return X, y, feature_columns
    
    def initialize_models(self) -> Dict[str, Any]:
        """
        Initialize all machine learning models
        """
        print("🤖 Initializing ML models...")
        
        models = {
            'Random Forest': RandomForestClassifier(
                n_estimators=100,
                max_depth=10,
                min_samples_split=5,
                min_samples_leaf=2,
                random_state=42,
                n_jobs=-1
            ),
            
            'Gradient Boosting': GradientBoostingClassifier(
                n_estimators=100,
                learning_rate=0.1,
                max_depth=6,
                random_state=42
            ),
            
            'Logistic Regression': LogisticRegression(
                max_iter=1000,
                random_state=42,
                n_jobs=-1
            ),
            
            'SVM': SVC(
                C=1.0,
                kernel='rbf',
                probability=True,
                random_state=42
            ),
            
            'Naive Bayes': GaussianNB(),
            
            'Decision Tree': DecisionTreeClassifier(
                max_depth=10,
                min_samples_split=5,
                min_samples_leaf=2,
                random_state=42
            ),
            
            'Neural Network': MLPClassifier(
                hidden_layer_sizes=(100, 50),
                max_iter=500,
                random_state=42,
                early_stopping=True
            )
        }
        
        print(f"  ✅ Initialized {len(models)} models")
        return models
    
    def train_models(self, X: np.ndarray, y: np.ndarray, feature_names: List[str]) -> Dict[str, Dict]:
        """
        Train all models and evaluate performance
        """
        print("🏋️ Training models...")
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Feature selection
        X_train_selected = self.feature_selector.fit_transform(X_train_scaled, y_train)
        X_test_selected = self.feature_selector.transform(X_test_scaled)
        
        models = self.initialize_models()
        results = {}
        
        for name, model in models.items():
            print(f"\n  🔄 Training {name}...")
            
            try:
                # Train model
                start_time = datetime.now()
                model.fit(X_train_selected, y_train)
                training_time = (datetime.now() - start_time).total_seconds()
                
                # Make predictions
                y_pred = model.predict(X_test_selected)
                y_pred_proba = model.predict_proba(X_test_selected)[:, 1] if hasattr(model, 'predict_proba') else None
                
                # Calculate metrics
                metrics = {
                    'accuracy': accuracy_score(y_test, y_pred),
                    'precision': precision_score(y_test, y_pred, average='weighted'),
                    'recall': recall_score(y_test, y_pred, average='weighted'),
                    'f1': f1_score(y_test, y_pred, average='weighted'),
                    'training_time': training_time
                }
                
                if y_pred_proba is not None:
                    metrics['auc_roc'] = roc_auc_score(y_test, y_pred_proba)
                
                # Cross-validation
                cv_scores = cross_val_score(model, X_train_selected, y_train, cv=5, scoring='accuracy')
                metrics['cv_mean'] = cv_scores.mean()
                metrics['cv_std'] = cv_scores.std()
                
                results[name] = {
                    'model': model,
                    'metrics': metrics,
                    'predictions': y_pred,
                    'probabilities': y_pred_proba
                }
                
                print(f"    ✅ Accuracy: {metrics['accuracy']:.4f}")
                print(f"    ✅ F1-Score: {metrics['f1']:.4f}")
                print(f"    ✅ CV Score: {metrics['cv_mean']:.4f} (+/- {metrics['cv_std']*2:.4f})")
                
            except Exception as e:
                print(f"    ❌ Error training {name}: {e}")
                continue
        
        # Create ensemble model
        if len(results) >= 3:
            print("\n  🔄 Creating Ensemble Model...")
            try:
                # Select top 3 models for ensemble
                top_models = sorted(results.items(), key=lambda x: x[1]['metrics']['f1'], reverse=True)[:3]
                
                ensemble_estimators = [(name, result['model']) for name, result in top_models]
                ensemble = VotingClassifier(estimators=ensemble_estimators, voting='soft')
                
                # Train ensemble
                start_time = datetime.now()
                ensemble.fit(X_train_selected, y_train)
                training_time = (datetime.now() - start_time).total_seconds()
                
                # Evaluate ensemble
                y_pred_ensemble = ensemble.predict(X_test_selected)
                y_pred_proba_ensemble = ensemble.predict_proba(X_test_selected)[:, 1]
                
                ensemble_metrics = {
                    'accuracy': accuracy_score(y_test, y_pred_ensemble),
                    'precision': precision_score(y_test, y_pred_ensemble, average='weighted'),
                    'recall': recall_score(y_test, y_pred_ensemble, average='weighted'),
                    'f1': f1_score(y_test, y_pred_ensemble, average='weighted'),
                    'auc_roc': roc_auc_score(y_test, y_pred_proba_ensemble),
                    'training_time': training_time
                }
                
                cv_scores_ensemble = cross_val_score(ensemble, X_train_selected, y_train, cv=5, scoring='accuracy')
                ensemble_metrics['cv_mean'] = cv_scores_ensemble.mean()
                ensemble_metrics['cv_std'] = cv_scores_ensemble.std()
                
                results['Ensemble'] = {
                    'model': ensemble,
                    'metrics': ensemble_metrics,
                    'predictions': y_pred_ensemble,
                    'probabilities': y_pred_proba_ensemble
                }
                
                print(f"    ✅ Ensemble Accuracy: {ensemble_metrics['accuracy']:.4f}")
                print(f"    ✅ Ensemble F1-Score: {ensemble_metrics['f1']:.4f}")
                
            except Exception as e:
                print(f"    ❌ Error creating ensemble: {e}")
        
        return results
    
    def select_best_model(self, results: Dict[str, Dict]) -> Tuple[str, Any]:
        """
        Select the best performing model
        """
        print("\n🏆 Selecting best model...")
        
        # Rank models by F1 score (weighted by AUC if available)
        model_scores = {}
        
        for name, result in results.items():
            metrics = result['metrics']
            # Combine F1 and AUC scores
            if 'auc_roc' in metrics:
                score = 0.7 * metrics['f1'] + 0.3 * metrics['auc_roc']
            else:
                score = metrics['f1']
            model_scores[name] = score
        
        best_model_name = max(model_scores.keys(), key=lambda k: model_scores[k])
        best_model = results[best_model_name]['model']
        
        print(f"  🥇 Best model: {best_model_name}")
        print(f"  📊 Combined score: {model_scores[best_model_name]:.4f}")
        
        return best_model_name, best_model
    
    def save_model(self, model: Any, model_name: str, feature_names: List[str]) -> str:
        """
        Save the trained model and associated components
        """
        print(f"\n💾 Saving model...")
        
        # Create model info
        model_info = {
            'model': model,
            'scaler': self.scaler,
            'feature_selector': self.feature_selector,
            'label_encoder': self.label_encoder,
            'feature_names': feature_names,
            'model_name': model_name,
            'trained_date': datetime.now().isoformat(),
            'version': '1.0'
        }
        
        # Save model
        model_path = os.path.join(self.models_dir, 'phishing_classifier.pkl')
        with open(model_path, 'wb') as f:
            pickle.dump(model_info, f)
        
        # Also save with joblib for better sklearn compatibility
        joblib_path = os.path.join(self.models_dir, 'phishing_classifier_joblib.pkl')
        joblib.dump(model_info, joblib_path)
        
        print(f"  ✅ Model saved to: {model_path}")
        print(f"  ✅ Joblib model saved to: {joblib_path}")
        
        return model_path
    
    def generate_model_report(self, results: Dict[str, Dict], best_model_name: str) -> str:
        """
        Generate comprehensive model evaluation report
        """
        print("\n📋 Generating model report...")
        
        report = []
        report.append("# Phishing Detection Model Training Report")
        report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**Best Model:** {best_model_name}")
        report.append("\n## Model Performance Comparison\n")
        
        # Create performance table
        report.append("| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC | CV Mean | Training Time |")
        report.append("|-------|----------|-----------|--------|----------|---------|---------|---------------|")
        
        for name, result in results.items():
            metrics = result['metrics']
            auc = f"{metrics.get('auc_roc', 0):.4f}" if 'auc_roc' in metrics else "N/A"
            report.append(
                f"| {name} | {metrics['accuracy']:.4f} | {metrics['precision']:.4f} | "
                f"{metrics['recall']:.4f} | {metrics['f1']:.4f} | {auc} | "
                f"{metrics['cv_mean']:.4f} | {metrics['training_time']:.2f}s |"
            )
        
        report.append("\n## Best Model Details\n")
        best_result = results[best_model_name]
        best_metrics = best_result['metrics']
        
        for metric, value in best_metrics.items():
            if metric != 'training_time':
                report.append(f"- **{metric.upper()}:** {value:.4f}")
            else:
                report.append(f"- **{metric.upper()}:** {value:.2f} seconds")
        
        report.append("\n## Feature Importance\n")
        
        # Try to get feature importance if available
        best_model = best_result['model']
        if hasattr(best_model, 'feature_importances_'):
            # Get selected feature names
            selected_features = self.feature_selector.get_support(indices=True)
            
            if hasattr(self, 'feature_names'):
                selected_feature_names = [self.feature_names[i] for i in selected_features]
                
                importance_pairs = list(zip(selected_feature_names, best_model.feature_importances_))
                importance_pairs.sort(key=lambda x: x[1], reverse=True)
                
                report.append("Top 10 Important Features:")
                for i, (feature, importance) in enumerate(importance_pairs[:10]):
                    report.append(f"{i+1}. **{feature}:** {importance:.4f}")
        
        report_text = "\n".join(report)
        
        # Save report
        report_path = os.path.join(self.models_dir, 'training_report.md')
        with open(report_path, 'w') as f:
            f.write(report_text)
        
        print(f"  ✅ Report saved to: {report_path}")
        
        return report_text
    
    def train_complete_pipeline(self) -> str:
        """
        Execute the complete training pipeline
        """
        print("🚀 Starting complete model training pipeline...\n")
        
        try:
            # Load datasets
            df = self.load_datasets()
            
            # Prepare features
            X, y, feature_names = self.prepare_features(df)
            self.feature_names = feature_names
            
            # Train models
            results = self.train_models(X, y, feature_names)
            
            if not results:
                raise ValueError("No models were successfully trained!")
            
            # Select best model
            best_model_name, best_model = self.select_best_model(results)
            
            # Save model
            model_path = self.save_model(best_model, best_model_name, feature_names)
            
            # Generate report
            report = self.generate_model_report(results, best_model_name)
            
            print("\n🎉 Training pipeline completed successfully!")
            print(f"📁 Model saved at: {model_path}")
            print(f"📋 Report available at: {os.path.join(self.models_dir, 'training_report.md')}")
            
            return model_path
            
        except Exception as e:
            print(f"❌ Training pipeline failed: {e}")
            raise

def main():
    """
    Main training function
    """
    print("🔍 Phishing Detection Model Training")
    print("=" * 50)
    
    # Get the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, '..', 'data')
    models_dir = os.path.join(script_dir, '..', 'models')
    
    # Initialize trainer
    trainer = PhishingModelTrainer(data_dir=data_dir, models_dir=models_dir)
    
    try:
        # Train models
        model_path = trainer.train_complete_pipeline()
        
        print(f"\n✅ Training completed successfully!")
        print(f"📁 Trained model available at: {model_path}")
        
        return model_path
        
    except Exception as e:
        print(f"\n❌ Training failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
