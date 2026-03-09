import tkinter as tk
from tkinter import ttk, messagebox
from checker.core import evaluate_password_strength
from logger import get_logger

logger = get_logger(__name__)

class PasswordCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Label
        label = ttk.Label(self.root, text="Enter Password:", font=("Arial", 12))
        label.pack(pady=(20, 5))

        # Password Entry
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(self.root, textvariable=self.password_var, show="*",
                                        font=("Arial", 12), width=30)
        self.password_entry.pack(pady=5)
        self.password_entry.focus()

        # Check Button
        check_btn = ttk.Button(self.root, text="Check Strength", command=self.check_strength)
        check_btn.pack(pady=10)

        # Results Frame
        self.results_frame = ttk.Frame(self.root)
        self.results_frame.pack(pady=10, fill='x', padx=20)

        self.strength_label = ttk.Label(self.results_frame, text="", font=("Arial", 12, "bold"))
        self.strength_label.pack(pady=5)

        self.entropy_label = ttk.Label(self.results_frame, text="", font=("Arial", 10))
        self.entropy_label.pack(pady=5)

        self.feedback_text = tk.Text(self.results_frame, height=6, width=45, font=("Arial", 10), state='disabled')
        self.feedback_text.pack(pady=5)

    def check_strength(self):
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("Input Error", "Please enter a password.")
            return

        result = evaluate_password_strength(password)

        self.strength_label.config(text=f"Strength: {result['strength']}")
        self.entropy_label.config(text=f"Entropy: {result['entropy']:.2f} bits")

        self.feedback_text.config(state='normal')
        self.feedback_text.delete("1.0", tk.END)
        for fb in result['feedback']:
            self.feedback_text.insert(tk.END, f"- {fb}\n")
        self.feedback_text.config(state='disabled')

        logger.info(f"Password evaluated: Strength={result['strength']}, Entropy={result['entropy']:.2f}")

def run_gui():
    root = tk.Tk()
    app = PasswordCheckerApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
