from config import STRENGTH_THRESHOLDS
from .utils import has_uppercase, has_lowercase, has_digit, has_special_char, calculate_entropy
from .feedback import generate_feedback
from logger import get_logger

logger = get_logger(__name__)

def evaluate_password_strength(password: str) -> dict:
    try:
        score = 0
        if len(password) >= 8:
            score += 1
        if len(password) >= 12:
            score += 1
        if has_uppercase(password):
            score += 1
        if has_lowercase(password):
            score += 1
        if has_digit(password):
            score += 1
        if has_special_char(password):
            score += 1

        entropy = calculate_entropy(password)
        logger.debug(f"Calculated entropy: {entropy:.2f}")

        if entropy > 50:
            score += 1

        if score <= STRENGTH_THRESHOLDS['weak']:
            strength = 'Weak'
        elif score <= STRENGTH_THRESHOLDS['moderate']:
            strength = 'Moderate'
        else:
            strength = 'Strong'

        feedback = generate_feedback(password)
        if strength == 'Strong':
            feedback = ["Your password is strong."]
        else:
            feedback.append("Consider improving password strength.")

        return {
            'strength': strength,
            'score': score,
            'feedback': feedback,
            'entropy': entropy
        }
    except Exception as e:
        logger.error(f"Error in evaluating password strength: {e}")
        return {
            'strength': 'Unknown',
            'score': 0,
            'feedback': ['An error occurred during evaluation.'],
            'entropy': 0
        }
