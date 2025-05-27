import re
import math

def has_uppercase(password: str) -> bool:
    return bool(re.search(r'[A-Z]', password))

def has_lowercase(password: str) -> bool:
    return bool(re.search(r'[a-z]', password))

def has_digit(password: str) -> bool:
    return bool(re.search(r'\d', password))

def has_special_char(password: str) -> bool:
    return bool(re.search(r'[^A-Za-z0-9]', password))

def calculate_entropy(password: str) -> float:
    """Estimate entropy of password."""
    pool = 0
    if has_lowercase(password):
        pool += 26
    if has_uppercase(password):
        pool += 26
    if has_digit(password):
        pool += 10
    if has_special_char(password):
        pool += 32  # Approximate number of special chars
    if pool == 0:
        return 0
    return len(password) * math.log2(pool)
