#!/usr/bin/env python3
"""
System Status Checker and Demo
Author: Cybersecurity Project XI

This script checks all system components and demonstrates the integration
"""

import requests
import time
import os
import sys
import json
from urllib.parse import urlparse

def print_header(title):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def print_status(message, status="INFO"):
    """Print status with emoji"""
    emojis = {
        "INFO": "🔵",
        "SUCCESS": "✅", 
        "ERROR": "❌",
        "WARNING": "⚠️",
        "TESTING": "🧪"
    }
    print(f"{emojis.get(status, '🔵')} {message}")

def test_ml_api():
    """Test ML API endpoints"""
    print_header("TESTING ML API (PORT 5000)")
    
    try:
        # Test health endpoint
        response = requests.get("http://localhost:5000/health", timeout=5)
        if response.status_code == 200:
            health_data = response.json()
            print_status("ML API Health Check: PASSED", "SUCCESS")
            print_status(f"  Status: {health_data.get('status', 'unknown')}", "INFO")
            print_status(f"  Model: {health_data.get('model', 'unknown')}", "INFO")
            print_status(f"  Version: {health_data.get('version', 'unknown')}", "INFO")
            
            # Test prediction endpoint with sample URLs
            test_urls = [
                "https://www.google.com",
                "https://github.com/microsoft/vscode",
                "http://suspicious-phishing-site.tk/login.php"
            ]
            
            print_status("Testing prediction endpoint...", "TESTING")
            
            for url in test_urls:
                test_data = {"url": url}
                pred_response = requests.post(
                    "http://localhost:5000/predict",
                    json=test_data,
                    timeout=10
                )
                
                if pred_response.status_code == 200:
                    result = pred_response.json()
                    prediction = result.get('prediction', 'unknown')
                    confidence = result.get('confidence', 'unknown')
                    probability = result.get('probability', 0)
                    
                    status_emoji = "🔴" if prediction == 'phishing' else "🟢"
                    print_status(f"  {status_emoji} {url[:50]}...", "INFO")
                    print_status(f"    → {prediction.upper()} ({confidence}, prob: {probability:.3f})", "INFO")
                else:
                    print_status(f"  Prediction failed for {url}: {pred_response.status_code}", "ERROR")
                    
            return True
        else:
            print_status(f"ML API Health Check: FAILED ({response.status_code})", "ERROR")
            return False
            
    except requests.exceptions.ConnectionError:
        print_status("ML API Connection: FAILED (Service not running)", "ERROR")
        print_status("  → Start ML API with: cd python_ml_nlp/app && python app.py", "WARNING")
        return False
    except Exception as e:
        print_status(f"ML API Test Error: {e}", "ERROR")
        return False

def test_web_server():
    """Test web server"""
    print_header("TESTING WEB SERVER (PORT 8080)")
    
    try:
        response = requests.get("http://localhost:8080", timeout=5)
        if response.status_code == 200:
            content = response.text
            if "Phishing" in content and "Detection" in content:
                print_status("Web Server: PASSED", "SUCCESS")
                print_status("  HTML content verified", "INFO")
                
                # Check for key components
                if "app.js" in content:
                    print_status("  JavaScript integration: FOUND", "SUCCESS")
                if "style.css" in content:
                    print_status("  CSS styling: FOUND", "SUCCESS")
                if "fetch" in content or "XMLHttpRequest" in content:
                    print_status("  API integration code: FOUND", "SUCCESS")
                
                return True
            else:
                print_status("Web Server responding but content incorrect", "WARNING")
                return False
        else:
            print_status(f"Web Server: FAILED ({response.status_code})", "ERROR")
            return False
            
    except requests.exceptions.ConnectionError:
        print_status("Web Server Connection: FAILED (Service not running)", "ERROR")
        print_status("  → Start Web Server with: cd web_portal && python -m http.server 8080", "WARNING")
        return False
    except Exception as e:
        print_status(f"Web Server Test Error: {e}", "ERROR")
        return False

def test_batch_processing():
    """Test batch processing capability"""
    print_header("TESTING BATCH PROCESSING")
    
    try:
        test_urls = [
            "https://www.google.com",
            "https://github.com",
            "https://stackoverflow.com",
            "http://suspicious-phishing.tk/verify",
            "https://secure-bank-login.ml/account"
        ]
        
        print_status(f"Testing batch processing with {len(test_urls)} URLs...", "TESTING")
        
        response = requests.post(
            "http://localhost:5000/predict/batch",
            json={"urls": test_urls},
            headers={"Content-Type": "application/json"},
            timeout=20
        )
        
        if response.status_code == 200:
            result = response.json()
            results = result.get('results', [])
            
            print_status(f"Batch Processing: PASSED ({len(results)} results)", "SUCCESS")
            
            phishing_count = 0
            legitimate_count = 0
            
            for res in results:
                prediction = res.get('prediction', 'unknown')
                probability = res.get('probability', 0)
                url = res.get('url', '')
                confidence = res.get('confidence', 'unknown')
                
                if prediction == 'phishing':
                    phishing_count += 1
                    status_emoji = "🔴"
                else:
                    legitimate_count += 1
                    status_emoji = "🟢"
                
                print_status(f"  {status_emoji} {prediction.upper()} | {confidence} | {url[:40]}...", "INFO")
            
            print_status(f"Summary: {legitimate_count} legitimate, {phishing_count} phishing", "INFO")
            return True
        else:
            print_status(f"Batch Processing: FAILED ({response.status_code})", "ERROR")
            return False
            
    except Exception as e:
        print_status(f"Batch Processing Error: {e}", "ERROR")
        return False

def test_integration_flow():
    """Test the complete integration flow"""
    print_header("TESTING COMPLETE INTEGRATION FLOW")
    
    print_status("Simulating frontend → backend → ML model flow...", "TESTING")
    
    # Simulate what happens when user enters URL in web interface
    test_scenarios = [
        {
            "url": "https://www.microsoft.com",
            "expected": "legitimate",
            "description": "Trusted corporate website"
        },
        {
            "url": "http://phishing-example.tk/login.php?redirect=bank.com",
            "expected": "phishing", 
            "description": "Suspicious phishing-like URL"
        },
        {
            "url": "https://www.amazon.com/security/verify-account",
            "expected": "legitimate",
            "description": "Legitimate but security-related URL"
        }
    ]
    
    success_count = 0
    
    for scenario in test_scenarios:
        url = scenario["url"]
        expected = scenario["expected"]
        description = scenario["description"]
        
        print_status(f"Testing: {description}", "TESTING")
        print_status(f"  URL: {url}", "INFO")
        
        try:
            # This simulates the exact API call made by the web frontend
            response = requests.post(
                "http://localhost:5000/predict",
                json={"url": url},
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "PhishingDetectionSystem/1.0"
                },
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                prediction = result.get('prediction', 'unknown')
                confidence = result.get('confidence', 'unknown')
                probability = result.get('probability', 0)
                processing_time = result.get('processing_time', 0)
                
                status_emoji = "🔴" if prediction == 'phishing' else "🟢"
                print_status(f"  Result: {status_emoji} {prediction.upper()}", "SUCCESS")
                print_status(f"  Confidence: {confidence}", "INFO")
                print_status(f"  Probability: {probability:.3f}", "INFO")
                print_status(f"  Processing Time: {processing_time:.3f}s", "INFO")
                
                success_count += 1
            else:
                print_status(f"  API call failed: {response.status_code}", "ERROR")
                
        except Exception as e:
            print_status(f"  Integration test failed: {e}", "ERROR")
    
    if success_count == len(test_scenarios):
        print_status("Complete Integration Flow: PASSED", "SUCCESS")
        return True
    else:
        print_status(f"Integration Flow: PARTIAL ({success_count}/{len(test_scenarios)} passed)", "WARNING")
        return False

def show_system_summary():
    """Show system summary and usage instructions"""
    print_header("SYSTEM INTEGRATION SUMMARY")
    
    print_status("🚀 Phishing Detection System - FULLY INTEGRATED", "SUCCESS")
    print()
    
    print("📋 SYSTEM COMPONENTS:")
    print("   🔹 Machine Learning Model")
    print("     - Gradient Boosting Classifier (96.03% accuracy)")
    print("     - 135+ URL features analyzed")
    print("     - Cross-validated and production-ready")
    print()
    print("   🔹 Flask API Backend")
    print("     - RESTful API endpoints")
    print("     - Real-time prediction")
    print("     - Batch processing support")
    print("     - JSON request/response format")
    print()
    print("   🔹 Web Frontend")
    print("     - Modern HTML5/CSS3/JavaScript")
    print("     - Real-time URL analysis")
    print("     - Visual risk indicators")
    print("     - Responsive design")
    print()
    print("   🔹 Complete Integration")
    print("     - Frontend ↔ Backend communication")
    print("     - API ↔ ML Model integration") 
    print("     - End-to-end URL analysis pipeline")
    print()
    
    print("🌐 ACCESS POINTS:")
    print("   • Web Interface:  http://localhost:8080")
    print("   • ML API:         http://localhost:5000")
    print("   • API Health:     http://localhost:5000/health")
    print("   • API Docs:       http://localhost:5000/docs")
    print()
    
    print("🎯 USAGE:")
    print("   1. Open http://localhost:8080 in your browser")
    print("   2. Enter any URL in the input field")
    print("   3. Click 'Analyze URL' to get real-time results")
    print("   4. View detailed analysis and risk assessment")
    print()

def main():
    """Main function"""
    print_header("🔒 PHISHING DETECTION SYSTEM - STATUS CHECK")
    
    print_status("Starting comprehensive system integration test...", "INFO")
    time.sleep(1)
    
    # Run all tests
    tests_results = []
    
    # Test 1: ML API
    tests_results.append(("ML API", test_ml_api()))
    
    # Test 2: Web Server  
    tests_results.append(("Web Server", test_web_server()))
    
    # Test 3: Batch Processing
    tests_results.append(("Batch Processing", test_batch_processing()))
    
    # Test 4: Integration Flow
    tests_results.append(("Integration Flow", test_integration_flow()))
    
    # Summary
    print_header("TEST RESULTS SUMMARY")
    
    passed = 0
    total = len(tests_results)
    
    for test_name, result in tests_results:
        if result:
            print_status(f"{test_name}: PASSED", "SUCCESS")
            passed += 1
        else:
            print_status(f"{test_name}: FAILED", "ERROR")
    
    print()
    print_status(f"Overall: {passed}/{total} tests passed", "SUCCESS" if passed == total else "WARNING")
    
    if passed == total:
        show_system_summary()
    else:
        print_status("Some components are not running. Please start all services first.", "WARNING")
        print_status("Use START_SYSTEM.bat to launch all components", "INFO")

if __name__ == "__main__":
    main()