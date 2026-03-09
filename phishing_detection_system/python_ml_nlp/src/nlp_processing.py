#!/usr/bin/env python3
"""
NLP Processing Module for Phishing URL Detection
Author: Cybersecurity Project XI
Date: September 2025

This module provides comprehensive NLP and feature extraction capabilities
for analyzing URLs and detecting phishing attempts using various linguistic
and structural features.
"""

import re
import urllib.parse as urlparse
import tldextract
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
import string
import math
from collections import Counter
import whois
import requests
from datetime import datetime
import socket
import ssl
from urllib.parse import urljoin, urlparse

class URLFeatureExtractor:
    """
    Advanced URL feature extraction for phishing detection
    """
    
    def __init__(self):
        self.suspicious_words = [
            'secure', 'account', 'update', 'confirm', 'login', 'signin',
            'banking', 'verification', 'suspended', 'limited', 'verify',
            'urgent', 'immediate', 'expire', 'click', 'alert', 'warning',
            'paypal', 'amazon', 'microsoft', 'apple', 'google', 'facebook',
            'ebay', 'netflix', 'bank', 'credit', 'card', 'security'
        ]
        
        self.brand_names = [
            'paypal', 'amazon', 'microsoft', 'apple', 'google', 'facebook',
            'instagram', 'twitter', 'linkedin', 'ebay', 'netflix', 'spotify',
            'dropbox', 'adobe', 'yahoo', 'outlook', 'gmail', 'hotmail'
        ]
        
        self.suspicious_tlds = [
            '.tk', '.ml', '.ga', '.cf', '.top', '.click', '.download',
            '.stream', '.science', '.racing', '.party', '.review'
        ]
    
    def extract_all_features(self, url: str) -> Dict[str, float]:
        """
        Extract comprehensive features from URL
        """
        features = {}
        
        # Basic URL features
        features.update(self._extract_basic_features(url))
        
        # Lexical features
        features.update(self._extract_lexical_features(url))
        
        # Domain-based features
        features.update(self._extract_domain_features(url))
        
        # Content-based features (if accessible)
        features.update(self._extract_content_features(url))
        
        # Behavioral features
        features.update(self._extract_behavioral_features(url))
        
        return features
    
    def _extract_basic_features(self, url: str) -> Dict[str, float]:
        """
        Extract basic structural features from URL
        """
        parsed = urlparse.urlparse(url)
        
        return {
            'url_length': len(url),
            'hostname_length': len(parsed.netloc),
            'path_length': len(parsed.path),
            'query_length': len(parsed.query) if parsed.query else 0,
            'fragment_length': len(parsed.fragment) if parsed.fragment else 0,
            'num_dots': url.count('.'),
            'num_hyphens': url.count('-'),
            'num_underscores': url.count('_'),
            'num_slashes': url.count('/'),
            'num_questionmarks': url.count('?'),
            'num_equal_signs': url.count('='),
            'num_at_symbols': url.count('@'),
            'num_and_symbols': url.count('&'),
            'num_percent_signs': url.count('%'),
            'num_hash_signs': url.count('#'),
            'has_ip_address': self._has_ip_address(parsed.netloc),
            'has_port': 1 if parsed.port else 0,
            'is_https': 1 if parsed.scheme == 'https' else 0,
        }
    
    def _extract_lexical_features(self, url: str) -> Dict[str, float]:
        """
        Extract lexical and linguistic features
        """
        parsed = urlparse.urlparse(url)
        
        # Count digits and letters
        digits = sum(c.isdigit() for c in url)
        letters = sum(c.isalpha() for c in url)
        
        # Suspicious words count
        url_lower = url.lower()
        suspicious_count = sum(1 for word in self.suspicious_words if word in url_lower)
        
        # Brand names in different parts
        brand_in_subdomain = any(brand in parsed.netloc.lower() for brand in self.brand_names)
        brand_in_path = any(brand in parsed.path.lower() for brand in self.brand_names)
        
        return {
            'digit_ratio': digits / len(url) if len(url) > 0 else 0,
            'letter_ratio': letters / len(url) if len(url) > 0 else 0,
            'suspicious_words_count': suspicious_count,
            'brand_in_subdomain': 1 if brand_in_subdomain else 0,
            'brand_in_path': 1 if brand_in_path else 0,
            'entropy': self._calculate_entropy(url),
            'longest_word_length': self._get_longest_word_length(url),
            'avg_word_length': self._get_avg_word_length(url),
        }
    
    def _extract_domain_features(self, url: str) -> Dict[str, float]:
        """
        Extract domain-specific features
        """
        parsed = urlparse.urlparse(url)
        extracted = tldextract.extract(url)
        
        return {
            'subdomain_count': len([s for s in extracted.subdomain.split('.') if s]),
            'domain_length': len(extracted.domain),
            'tld_length': len(extracted.suffix),
            'has_www': 1 if 'www' in extracted.subdomain else 0,
            'suspicious_tld': 1 if any(tld in url.lower() for tld in self.suspicious_tlds) else 0,
            'domain_in_path': 1 if extracted.domain.lower() in parsed.path.lower() else 0,
            'tld_in_path': 1 if extracted.suffix.lower() in parsed.path.lower() else 0,
            'domain_age_days': self._get_domain_age(extracted.domain + '.' + extracted.suffix),
            'is_shortened_url': self._is_shortened_url(parsed.netloc),
        }
    
    def _extract_content_features(self, url: str) -> Dict[str, float]:
        """
        Extract content-based features (requires web scraping)
        """
        try:
            response = requests.get(url, timeout=5, allow_redirects=True)
            content = response.text.lower()
            
            return {
                'num_redirects': len(response.history),
                'has_login_form': 1 if 'login' in content or 'signin' in content else 0,
                'has_password_field': 1 if 'password' in content else 0,
                'external_links_ratio': self._calculate_external_links_ratio(content, url),
                'has_iframe': 1 if '<iframe' in content else 0,
                'has_popup': 1 if 'popup' in content or 'window.open' in content else 0,
                'favicon_external': self._has_external_favicon(content, url),
                'status_code': response.status_code,
            }
        except Exception:
            # Return default values if content analysis fails
            return {
                'num_redirects': 0,
                'has_login_form': 0,
                'has_password_field': 0,
                'external_links_ratio': 0.0,
                'has_iframe': 0,
                'has_popup': 0,
                'favicon_external': 0,
                'status_code': 0,
            }
    
    def _extract_behavioral_features(self, url: str) -> Dict[str, float]:
        """
        Extract behavioral and security-related features
        """
        parsed = urlparse.urlparse(url)
        extracted = tldextract.extract(url)
        
        return {
            'has_ssl_certificate': self._has_valid_ssl(parsed.netloc),
            'dns_resolves': self._dns_resolves(parsed.netloc),
            'whois_available': self._whois_available(parsed.netloc),
            'url_shortening_service': self._is_url_shortening_service(parsed.netloc),
            'double_slash_redirect': 1 if '//' in parsed.path else 0,
            'prefix_suffix_dash': 1 if '-' in extracted.domain else 0,
        }
    
    # Helper methods
    def _has_ip_address(self, netloc: str) -> int:
        """Check if netloc contains IP address"""
        ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        return 1 if re.search(ip_pattern, netloc) else 0
    
    def _calculate_entropy(self, text: str) -> float:
        """Calculate Shannon entropy of text"""
        if not text:
            return 0.0
        
        counts = Counter(text)
        entropy = 0.0
        for count in counts.values():
            prob = count / len(text)
            entropy -= prob * math.log2(prob)
        
        return entropy
    
    def _get_longest_word_length(self, url: str) -> int:
        """Get length of longest word in URL"""
        words = re.findall(r'[a-zA-Z]+', url)
        return max(len(word) for word in words) if words else 0
    
    def _get_avg_word_length(self, url: str) -> float:
        """Get average word length in URL"""
        words = re.findall(r'[a-zA-Z]+', url)
        return sum(len(word) for word in words) / len(words) if words else 0.0
    
    def _get_domain_age(self, domain: str) -> float:
        """Get domain age in days"""
        try:
            w = whois.whois(domain)
            if w.creation_date:
                if isinstance(w.creation_date, list):
                    creation_date = w.creation_date[0]
                else:
                    creation_date = w.creation_date
                
                age = (datetime.now() - creation_date).days
                return float(age)
        except Exception:
            pass
        return -1.0  # Unknown age
    
    def _is_shortened_url(self, netloc: str) -> int:
        """Check if URL uses a shortening service"""
        shortening_services = [
            'bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'short.link',
            'ow.ly', 'buff.ly', 'is.gd', 'v.gd', 'x.co'
        ]
        return 1 if any(service in netloc.lower() for service in shortening_services) else 0
    
    def _calculate_external_links_ratio(self, content: str, base_url: str) -> float:
        """Calculate ratio of external links"""
        try:
            parsed_base = urlparse.urlparse(base_url)
            base_domain = parsed_base.netloc
            
            # Find all links
            links = re.findall(r'href=["\']([^"\'>]+)["\']', content)
            
            if not links:
                return 0.0
            
            external_count = 0
            for link in links:
                parsed_link = urlparse.urlparse(urljoin(base_url, link))
                if parsed_link.netloc and parsed_link.netloc != base_domain:
                    external_count += 1
            
            return external_count / len(links)
        except Exception:
            return 0.0
    
    def _has_external_favicon(self, content: str, base_url: str) -> int:
        """Check if favicon is hosted externally"""
        try:
            parsed_base = urlparse.urlparse(base_url)
            base_domain = parsed_base.netloc
            
            favicon_match = re.search(r'<link[^>]*rel=["\'](?:shortcut )?icon["\'][^>]*href=["\']([^"\'>]+)["\']', content)
            if favicon_match:
                favicon_url = favicon_match.group(1)
                parsed_favicon = urlparse.urlparse(urljoin(base_url, favicon_url))
                return 1 if parsed_favicon.netloc and parsed_favicon.netloc != base_domain else 0
        except Exception:
            pass
        return 0
    
    def _has_valid_ssl(self, netloc: str) -> int:
        """Check if domain has valid SSL certificate"""
        try:
            # Remove port if present
            hostname = netloc.split(':')[0]
            
            context = ssl.create_default_context()
            with socket.create_connection((hostname, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert()
                    return 1 if cert else 0
        except Exception:
            return 0
    
    def _dns_resolves(self, netloc: str) -> int:
        """Check if domain resolves via DNS"""
        try:
            hostname = netloc.split(':')[0]
            socket.gethostbyname(hostname)
            return 1
        except Exception:
            return 0
    
    def _whois_available(self, netloc: str) -> int:
        """Check if WHOIS information is available"""
        try:
            hostname = netloc.split(':')[0]
            w = whois.whois(hostname)
            return 1 if w and w.domain_name else 0
        except Exception:
            return 0
    
    def _is_url_shortening_service(self, netloc: str) -> int:
        """Check if this is a URL shortening service"""
        return self._is_shortened_url(netloc)

class TextPreprocessor:
    """
    Text preprocessing utilities for NLP analysis
    """
    
    @staticmethod
    def clean_url(url: str) -> str:
        """Clean and normalize URL for analysis"""
        # Remove protocol
        url = re.sub(r'^https?://', '', url)
        
        # Remove www
        url = re.sub(r'^www\.', '', url)
        
        # Convert to lowercase
        url = url.lower()
        
        # Remove trailing slash
        url = url.rstrip('/')
        
        return url
    
    @staticmethod
    def extract_words_from_url(url: str) -> List[str]:
        """Extract meaningful words from URL"""
        # Remove protocol and www
        cleaned_url = TextPreprocessor.clean_url(url)
        
        # Split by common delimiters
        words = re.split(r'[./-_=&?#%]+', cleaned_url)
        
        # Filter out empty strings and single characters
        words = [word for word in words if len(word) > 1]
        
        # Remove numbers-only strings
        words = [word for word in words if not word.isdigit()]
        
        return words
    
    @staticmethod
    def calculate_similarity(url1: str, url2: str) -> float:
        """Calculate similarity between two URLs"""
        words1 = set(TextPreprocessor.extract_words_from_url(url1))
        words2 = set(TextPreprocessor.extract_words_from_url(url2))
        
        if not words1 and not words2:
            return 1.0
        
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        return intersection / union if union > 0 else 0.0

def analyze_url_batch(urls: List[str]) -> pd.DataFrame:
    """
    Analyze a batch of URLs and return feature DataFrame
    """
    extractor = URLFeatureExtractor()
    results = []
    
    for url in urls:
        try:
            features = extractor.extract_all_features(url)
            features['url'] = url
            results.append(features)
        except Exception as e:
            print(f"Error processing URL {url}: {e}")
            continue
    
    return pd.DataFrame(results)

def preprocess_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess dataset for machine learning
    """
    # Handle missing values
    df = df.fillna(0)
    
    # Normalize numerical features
    numerical_columns = df.select_dtypes(include=[np.number]).columns
    for col in numerical_columns:
        if col != 'status' and col != 'CLASS_LABEL':  # Don't normalize target variables
            df[col] = (df[col] - df[col].mean()) / (df[col].std() + 1e-8)
    
    return df

if __name__ == "__main__":
    # Test the feature extraction
    test_urls = [
        'https://www.google.com',
        'http://phishing-example.com/login.php?user=admin',
        'https://secure-bank-update.tk/verify-account.html'
    ]
    
    extractor = URLFeatureExtractor()
    for url in test_urls:
        print(f"\nAnalyzing: {url}")
        features = extractor.extract_all_features(url)
        for key, value in features.items():
            print(f"  {key}: {value}")
