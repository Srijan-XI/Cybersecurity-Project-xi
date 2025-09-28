# Phishing Detection Model Training Report
**Generated:** 2025-09-29 01:31:53
**Best Model:** Gradient Boosting

## Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC | CV Mean | Training Time |
|-------|----------|-----------|--------|----------|---------|---------|---------------|
| Random Forest | 0.9536 | 0.9537 | 0.9536 | 0.9536 | 0.9880 | 0.9518 | 0.30s |
| Gradient Boosting | 0.9603 | 0.9604 | 0.9603 | 0.9603 | 0.9902 | 0.9561 | 4.21s |
| Logistic Regression | 0.9029 | 0.9029 | 0.9029 | 0.9029 | 0.9632 | 0.9023 | 1.87s |
| SVM | 0.9293 | 0.9303 | 0.9293 | 0.9293 | 0.9785 | 0.9234 | 22.17s |
| Naive Bayes | 0.8147 | 0.8315 | 0.8147 | 0.8124 | 0.9171 | 0.8122 | 0.01s |
| Decision Tree | 0.9442 | 0.9443 | 0.9442 | 0.9442 | 0.9671 | 0.9409 | 0.05s |
| Neural Network | 0.9533 | 0.9533 | 0.9533 | 0.9533 | 0.9865 | 0.9424 | 3.35s |
| Ensemble | 0.9580 | 0.9580 | 0.9580 | 0.9580 | 0.9897 | 0.9538 | 6.97s |

## Best Model Details

- **ACCURACY:** 0.9603
- **PRECISION:** 0.9604
- **RECALL:** 0.9603
- **F1:** 0.9603
- **TRAINING_TIME:** 4.21 seconds
- **AUC_ROC:** 0.9902
- **CV_MEAN:** 0.9561
- **CV_STD:** 0.0030

## Feature Importance

Top 10 Important Features:
1. **PctExtNullSelfRedirectHyperlinksRT:** 0.2677
2. **google_index:** 0.2049
3. **page_rank:** 0.1428
4. **PctExtHyperlinks:** 0.1043
5. **nb_hyperlinks:** 0.0688
6. **nb_www:** 0.0343
7. **FrequentDomainNameMismatch:** 0.0333
8. **domain_age:** 0.0213
9. **PctNullSelfRedirectHyperlinks:** 0.0201
10. **NumDash:** 0.0134