import unittest2
from checker.core import evaluate_password_strength

class TestPasswordStrength(unittest2.TestCase):
    def test_weak_password(self):
        result = evaluate_password_strength('abc')
        self.assertEqual(result['strength'], 'Weak')

    def test_moderate_password(self):
        result = evaluate_password_strength('Abcdef12')
        self.assertEqual(result['strength'], 'Moderate')

    def test_strong_password(self):
        result = evaluate_password_strength('Abcdef12$%^&')
        self.assertEqual(result['strength'], 'Strong')

if __name__ == '__main__':
    unittest2.main()
