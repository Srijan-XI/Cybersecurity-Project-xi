# 🔐 Password Strength Checker

A production-ready Password Strength Checker built with a modular architecture, featuring a graphical user interface (GUI), command-line interface (CLI), and comprehensive unit testing. Designed to align with cybersecurity best practices, this tool empowers users to evaluate password strength and encourage secure credential habits.

---

## 📦 Features

- ✅ **Real-Time Password Analysis** with entropy calculations
- ✅ **GUI with Tkinter** for user-friendly interaction
- ✅ **CLI Mode** for terminal-based evaluations
- ✅ **Modular Structure** using Python best practices
- ✅ **Comprehensive Unit Testing** with detailed test coverage
- ✅ **Customizable Configuration** file for strength thresholds
- ✅ **Structured Logging** for security auditing and debugging
- ✅ **Intelligent Feedback System** with actionable recommendations
- ✅ **Cross-platform Compatibility** (Windows, macOS, Linux)

---

## 🗂️ Project Structure

```
password_strength_checker/
├── main.py                 # CLI application entry point
├── run_gui.py             # GUI application entry point
├── config.py              # Configuration settings and thresholds
├── logger.py              # Logging configuration
├── README.md              # Project documentation
├── checker/               # Core password evaluation logic
│   ├── core.py           # Main password strength evaluation
│   ├── feedback.py       # User feedback generation
│   └── utils.py          # Utility functions (entropy, character checks)
├── gui/                   # Graphical user interface
│   └── app.py            # Tkinter GUI implementation
└── test/                  # Unit tests
    └── test_core.py      # Core functionality tests
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- tkinter (usually included with Python)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Srijan-XI/Cybersecurity-Project-xi/tree/main/password_strength_checker.git
   cd password-strength-checker
   ```

2. **No additional dependencies required** - uses only Python standard library!

### Usage

#### GUI Mode (Recommended)
```bash
python run_gui.py
```

#### CLI Mode
```bash
python main.py
```

---

## 💻 Usage Examples

### Command Line Interface
```bash
$ python main.py
Welcome to Password Strength Checker
Enter password to evaluate (or type 'e' to quit): MySecureP@ssw0rd!

Strength: Strong
Score: 6
Entropy: 65.42 bits
Feedback:
- Great! Your password meets all security requirements.
```

### Graphical User Interface
- Launch the GUI with `python run_gui.py`
- Enter your password in the input field
- View real-time strength analysis and feedback
- Get actionable recommendations for improvement

---

## 🔧 Configuration

Customize password strength thresholds in `config.py`:

```python
STRENGTH_THRESHOLDS = {
    'WEAK': 0,      # 0-2 criteria met
    'MEDIUM': 3,    # 3-4 criteria met  
    'STRONG': 5     # 5+ criteria met
}
```

### Evaluation Criteria

The password strength is evaluated based on:
- **Length**: Minimum 8 characters (bonus for 12+)
- **Uppercase Letters**: A-Z
- **Lowercase Letters**: a-z
- **Digits**: 0-9
- **Special Characters**: !@#$%^&*()_+-=[]{}|;:,.<>?
- **Entropy**: Mathematical measure of randomness

---

## 🧪 Testing

Run the test suite to ensure everything works correctly:

```bash
# Run all tests
python -m unittest test.test_core

# Run with verbose output
python -m unittest test.test_core -v
```

### Test Coverage
- Password strength evaluation
- Character type detection
- Entropy calculations
- Feedback generation
- Edge cases and error handling

---

## 📊 Security Features

### Entropy Calculation
- Uses mathematical entropy to measure password unpredictability
- Higher entropy = stronger password
- Considers character set size and password length

### Secure Practices
- **No password storage**: Passwords are never saved or logged
- **Memory safety**: Passwords are not retained after evaluation
- **Local processing**: All analysis happens locally on your machine

---

## 🛠️ Development

### Adding New Features

1. **Core Logic**: Extend `checker/core.py` for new evaluation criteria
2. **Feedback**: Update `checker/feedback.py` for new user messages
3. **GUI**: Modify `gui/app.py` for interface improvements
4. **Tests**: Add tests in `test/` directory

### Code Style
- Follow PEP 8 guidelines
- Use type hints where applicable
- Maintain modular structure
- Add comprehensive docstrings

---

## 📝 Logging

The application logs important events to help with debugging and security auditing:

- Password evaluation attempts (without storing actual passwords)
- Error conditions and exceptions
- Application startup and shutdown events

Configure logging levels in `logger.py`.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 🔒 Security Notice

This tool is designed for educational and personal use. For enterprise applications, consider additional security measures such as:
- Integration with breach databases
- Advanced pattern detection
- Policy enforcement mechanisms
- Audit trails and compliance features

---

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the test suite for usage examples
- Review the code documentation

---

**Built with ❤️ for cybersecurity awareness and education.**

