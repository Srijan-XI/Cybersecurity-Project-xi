from checker.core import evaluate_password_strength
from logger import get_logger

logger = get_logger(__name__)

def main():
    print("Welcome to Password Strength Checker")
    while True:
        password = input("Enter password to evaluate (or type 'e' to quit): ")
        if password.lower() == 'e':
            print("Exiting Password Strength Checker.")
            break

        result = evaluate_password_strength(password)
        print(f"\nStrength: {result['strength']}")
        print(f"Score: {result['score']}")
        print(f"Entropy: {result['entropy']:.2f} bits")
        print("Feedback:")
        for fb in result['feedback']:
            print(f"- {fb}")
        print("\n" + "-"*40 + "\n")

if __name__ == "__main__":
    main()
