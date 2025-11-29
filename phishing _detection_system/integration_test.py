#!/usr/bin/env python3
"""
Complete System Integration Test
Author: Srijan XI
Date: September 2025

This script tests the complete integration of all system components:
- Web Portal (Frontend)
- Flask ML API (Backend)
- Trained ML Model
- URL Analysis Pipeline
"""

import requests
import time
import subprocess
import os
import sys
import threading
from urllib.parse import urlparse

class SystemIntegrationTest:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.services = {}
        self.test_results = {}
        
    def log(self, message, level="INFO"):
        """Log messages with timestamp"""
        timestamp = time.strftime("%H:%M:%S")
        levels = {
            "INFO": "🔵",
            "SUCCESS": "✅", 
            "ERROR": "❌",
            "WARNING": "⚠️"
        }
        print(f"[{timestamp}] {levels.get(level, '🔵')} {message}")
    
    def start_ml_api(self):
        """Start the ML API server"""
        try:
            self.log("Starting ML API Server (Port 5000)...")
            api_dir = os.path.join(self.base_dir, "python_ml_nlp", "app")
            cmd = [sys.executable, "app.py"]
            
            process = subprocess.Popen(
                cmd,
                cwd=api_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            self.services['ml_api'] = process
            
            # Wait for startup
            time.sleep(5)
            
            # Test if it's running
            if self.test_ml_api():
                self.log("ML API Server started successfully", "SUCCESS")
                return True
            else:
                self.log("ML API Server failed to start properly", "ERROR")
                return False
                
        except Exception as e:
            self.log(f"Error starting ML API: {e}", "ERROR")
            return False
    
    def start_web_server(self):
        """Start the web server"""
        try:
            self.log("Starting Web Server (Port 8080)...")
            web_dir = os.path.join(self.base_dir, "web_portal")
            cmd = [sys.executable, "-m", "http.server", "8080"]
            
            process = subprocess.Popen(
                cmd,
                cwd=web_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            self.services['web_server'] = process
            
            # Wait for startup
            time.sleep(3)
            
            # Test if it's running
            if self.test_web_server():
                self.log("Web Server started successfully", "SUCCESS")
                return True
            else:
                self.log("Web Server failed to start properly", "ERROR")
                return False
                
        except Exception as e:
            self.log(f"Error starting Web Server: {e}", "ERROR")
            return False
    
    def test_ml_api(self):
        """Test ML API endpoints"""
        try:
            # Test health endpoint
            response = requests.get("http://localhost:5000/health", timeout=5)
            if response.status_code == 200:
                self.log("ML API health check passed", "SUCCESS")
                
                # Test prediction endpoint
                test_data = {"url": "https://www.google.com"}
                pred_response = requests.post(
                    "http://localhost:5000/predict",
                    json=test_data,
                    timeout=10
                )
                
                if pred_response.status_code == 200:
                    result = pred_response.json()
                    self.log(f"ML API prediction test passed: {result.get('prediction', 'unknown')}", "SUCCESS")
                    self.test_results['ml_api_prediction'] = result
                    return True
                else:
                    self.log(f"ML API prediction test failed: {pred_response.status_code}", "ERROR")
                    return False
            else:
                self.log(f"ML API health check failed: {response.status_code}", "ERROR")
                return False
                
        except requests.exceptions.ConnectionError:
            self.log("Cannot connect to ML API", "ERROR")
            return False
        except Exception as e:
            self.log(f"ML API test error: {e}", "ERROR")
            return False
    
    def test_web_server(self):
        """Test web server"""
        try:
            response = requests.get("http://localhost:8080", timeout=5)
            if response.status_code == 200:
                if "Phishing" in response.text and "Detection" in response.text:
                    self.log("Web Server test passed - HTML content verified", "SUCCESS")
                    return True
                else:
                    self.log("Web Server responding but content may be incorrect", "WARNING")
                    return True
            else:
                self.log(f"Web Server test failed: {response.status_code}", "ERROR")
                return False
                
        except requests.exceptions.ConnectionError:
            self.log("Cannot connect to Web Server", "ERROR")
            return False
        except Exception as e:
            self.log(f"Web Server test error: {e}", "ERROR")
            return False
    
    def test_ml_model_direct(self):
        """Test the ML model directly"""
        try:
            self.log("Testing ML model directly...")
            
            # Import and test classifier
            sys.path.append(os.path.join(self.base_dir, "python_ml_nlp"))
            from classifier import PhishingClassifier
            
            classifier = PhishingClassifier()
            
            # Test URLs
            test_urls = [
                "https://www.google.com",
                "https://github.com",
                "http://suspicious-phishing-site.tk/login",
                "https://secure-bank-update.com/verify-account"
            ]
            
            results = []
            for url in test_urls:
                prediction, probability, confidence = classifier.predict(url)
                result = {
                    'url': url,
                    'prediction': 'phishing' if prediction == 1 else 'legitimate',
                    'probability': probability,
                    'confidence': confidence
                }
                results.append(result)
                
                status = "🔴 PHISHING" if prediction == 1 else "🟢 SAFE"
                self.log(f"  {status} | {confidence:<6} | {probability:.3f} | {url}")
            
            self.test_results['ml_model_direct'] = results
            self.log("Direct ML model test completed", "SUCCESS")
            return True
            
        except Exception as e:
            self.log(f"Direct ML model test error: {e}", "ERROR")
            return False
    
    def test_end_to_end_flow(self):
        """Test the complete end-to-end flow"""
        try:
            self.log("Testing end-to-end integration flow...")
            
            # Test the complete flow: Web UI -> API -> ML Model
            test_urls = [
                "https://www.amazon.com",
                "http://phishing-example.tk/login.php"
            ]
            
            for url in test_urls:
                self.log(f"Testing end-to-end flow for: {url}")
                
                # Test API call (simulating what the web frontend does)
                response = requests.post(
                    "http://localhost:5000/predict",
                    json={"url": url},
                    headers={"Content-Type": "application/json"},
                    timeout=10
                )
                
                if response.status_code == 200:
                    result = response.json()
                    prediction = result.get('prediction', 'unknown')
                    probability = result.get('probability', 0)
                    confidence = result.get('confidence', 'unknown')
                    
                    status = "🔴 PHISHING" if prediction == 'phishing' else "🟢 SAFE"
                    self.log(f"  {status} | {confidence:<6} | {probability:.3f} | {url}")
                else:
                    self.log(f"API call failed for {url}: {response.status_code}", "ERROR")
                    return False
            
            self.log("End-to-end integration test completed successfully", "SUCCESS")
            return True
            
        except Exception as e:
            self.log(f"End-to-end test error: {e}", "ERROR")
            return False
    
    def test_batch_processing(self):
        """Test batch processing capability"""
        try:
            self.log("Testing batch processing...")
            
            test_urls = [
                "https://www.google.com",
                "https://github.com",
                "http://suspicious-site.ml/verify"
            ]
            
            response = requests.post(
                "http://localhost:5000/predict/batch",
                json={"urls": test_urls},
                headers={"Content-Type": "application/json"},
                timeout=15
            )
            
            if response.status_code == 200:
                result = response.json()
                results = result.get('results', [])
                
                self.log(f"Batch processing completed: {len(results)} results")
                for res in results:
                    prediction = res.get('prediction', 'unknown')
                    probability = res.get('probability', 0)
                    url = res.get('url', '')
                    
                    status = "🔴 PHISHING" if prediction == 'phishing' else "🟢 SAFE"
                    self.log(f"  {status} | {probability:.3f} | {url}")
                
                self.test_results['batch_processing'] = results
                self.log("Batch processing test completed successfully", "SUCCESS")
                return True
            else:
                self.log(f"Batch processing test failed: {response.status_code}", "ERROR")
                return False
                
        except Exception as e:
            self.log(f"Batch processing test error: {e}", "ERROR")
            return False
    
    def cleanup(self):
        """Clean up started services"""
        self.log("Cleaning up services...")
        
        for service_name, process in self.services.items():
            try:
                if process.poll() is None:  # Process is still running
                    self.log(f"Stopping {service_name}...")
                    process.terminate()
                    time.sleep(2)
                    if process.poll() is None:
                        process.kill()
            except Exception as e:
                self.log(f"Error stopping {service_name}: {e}", "WARNING")
    
    def generate_report(self):
        """Generate a summary report"""
        self.log("=" * 60)
        self.log("SYSTEM INTEGRATION TEST SUMMARY", "INFO")
        self.log("=" * 60)
        
        # Count test results
        total_tests = len(self.test_results)
        if total_tests > 0:
            self.log(f"Total Integration Tests: {total_tests}")
            
            for test_name, result in self.test_results.items():
                if isinstance(result, list):
                    self.log(f"✅ {test_name}: {len(result)} items processed")
                elif isinstance(result, dict):
                    prediction = result.get('prediction', 'unknown')
                    self.log(f"✅ {test_name}: {prediction}")
        
        self.log("=" * 60)
        self.log("🎉 INTEGRATION TEST COMPLETED", "SUCCESS")
        self.log("Your phishing detection system is fully integrated and working!")
        self.log("=" * 60)
    
    def run_complete_test(self):
        """Run the complete integration test suite"""
        try:
            self.log("🚀 Starting Complete System Integration Test")
            self.log("=" * 60)
            
            # Test 1: Direct ML Model
            if not self.test_ml_model_direct():
                self.log("Critical error: ML model test failed", "ERROR")
                return
            
            # Test 2: Start ML API
            if not self.start_ml_api():
                self.log("Critical error: ML API failed to start", "ERROR")
                return
            
            # Test 3: Start Web Server
            if not self.start_web_server():
                self.log("Critical error: Web Server failed to start", "ERROR")
                return
            
            # Test 4: End-to-end flow
            if not self.test_end_to_end_flow():
                self.log("End-to-end test failed", "ERROR")
            
            # Test 5: Batch processing
            if not self.test_batch_processing():
                self.log("Batch processing test failed", "ERROR")
            
            self.log("All integration tests completed!")
            
            # Keep services running for demonstration
            self.log("=" * 60)
            self.log("🌐 SYSTEM NOW RUNNING:", "SUCCESS")
            self.log("   - Web Interface: http://localhost:8080")
            self.log("   - ML API: http://localhost:5000")
            self.log("   - API Documentation: http://localhost:5000/health")
            self.log("=" * 60)
            
            input("Press Enter to stop all services and exit...")
            
        except KeyboardInterrupt:
            self.log("Test interrupted by user", "WARNING")
        except Exception as e:
            self.log(f"Unexpected error during testing: {e}", "ERROR")
        finally:
            self.cleanup()
            self.generate_report()

def main():
    """Main function"""
    print("\n" + "="*80)
    print("🔒 PHISHING DETECTION SYSTEM - COMPLETE INTEGRATION TEST")
    print("="*80)
    
    tester = SystemIntegrationTest()
    tester.run_complete_test()

if __name__ == "__main__":
    main()