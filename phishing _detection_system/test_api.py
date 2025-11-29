#!/usr/bin/env python3
"""
Test script for the Phishing Detection API
"""

import requests
import json
import time

def test_api():
    """Test the phishing detection API"""
    print("🧪 Testing Phishing Detection API...")
    
    base_url = "http://localhost:5000"
    
    # Test URLs
    test_urls = [
        "https://www.google.com",
        "https://www.github.com",
        "http://suspicious-phishing-site.tk/login",
        "https://paypal-security-update.com/verify",
        "https://www.amazon.com",
        "http://secure-bank.ml/account-suspended"
    ]
    
    try:
        # Test health endpoint
        print("\n1. Testing health endpoint...")
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            health_data = response.json()
            print(f"   Status: {health_data.get('status', 'unknown')}")
            if 'model' in health_data:
                model_info = health_data['model']
                print(f"   Model: {model_info.get('model_name', 'unknown')}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return
        
        print(f"\n2. Testing single URL predictions...")
        print("-" * 60)
        
        for url in test_urls:
            try:
                payload = {"url": url}
                response = requests.post(
                    f"{base_url}/predict",
                    json=payload,
                    headers={"Content-Type": "application/json"}
                )
                
                if response.status_code == 200:
                    result = response.json()
                    prediction = result.get('prediction', 'unknown')
                    probability = result.get('probability', 0)
                    confidence = result.get('confidence', 'unknown')
                    
                    status_emoji = "🔴" if prediction == "phishing" else "🟢"
                    print(f"{status_emoji} {prediction.upper():<10} | {confidence:<6} | {probability:.3f} | {url}")
                else:
                    print(f"❌ Error for {url}: {response.status_code}")
                    
            except Exception as e:
                print(f"❌ Exception for {url}: {e}")
        
        print("-" * 60)
        
        # Test batch prediction
        print(f"\n3. Testing batch prediction...")
        try:
            batch_payload = {"urls": test_urls[:3]}  # Test with first 3 URLs
            response = requests.post(
                f"{base_url}/predict/batch",
                json=batch_payload,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                batch_result = response.json()
                results = batch_result.get('results', [])
                print(f"✅ Batch prediction successful ({len(results)} results)")
                
                for result in results:
                    prediction = result.get('prediction', 'unknown')
                    probability = result.get('probability', 0)
                    url = result.get('url', '')
                    status_emoji = "🔴" if prediction == "phishing" else "🟢"
                    print(f"   {status_emoji} {prediction.upper():<10} | {probability:.3f} | {url}")
            else:
                print(f"❌ Batch prediction failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Batch prediction exception: {e}")
        
        print(f"\n✅ API testing completed!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to API. Make sure the Flask server is running on localhost:5000")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")

if __name__ == "__main__":
    test_api()