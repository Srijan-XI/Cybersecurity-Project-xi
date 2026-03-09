from config import MIN_LENGTH

def generate_feedback(password: str) -> list:
    feedback = []
    if len(password) < MIN_LENGTH:
        feedback.append(f"Password should be at least {MIN_LENGTH} characters long.")
    if not any(c.isupper() for c in password):
        feedback.append("Add uppercase letters.")
    if not any(c.islower() for c in password):
        feedback.append("Add lowercase letters.")
    if not any(c.isdigit() for c in password):
        feedback.append("Include digits.")
    if not any(not c.isalnum() for c in password):
        feedback.append("Include special characters.")
    return feedback
