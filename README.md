# 🔐 Password Strength Analyzer

A Python-based cybersecurity mini project that analyzes password strength using character validation, common-password detection, and predictable-pattern detection.

## 🚀 Features

- Checks password length
- Detects uppercase letters
- Detects lowercase letters
- Detects numbers
- Detects special characters
- Detects common passwords
- Detects predictable sequences
- Detects repeated characters
- Calculates password strength
- Provides improvement suggestions

## 🛠️ Technologies Used

- Python 3
- Regular Expressions (`re`)
- Git
- GitHub

## ⚙️ How It Works

The analyzer evaluates a password using multiple security checks:

1. Minimum length of 8 characters
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one number
5. At least one special character
6. Common-password detection
7. Predictable-sequence detection
8. Repeated-character detection

The score determines the password strength:

| Score | Strength |
|---:|---|
| 0–2 | Weak |
| 3–4 | Medium |
| 5 | Strong |

## 🧪 Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| Strong Password | `BlueTiger#47Moon` | Strong |
| Medium Password | `ghost123` | Medium |
| Weak Password | `ghost` | Weak |
| Common Password | `password123` | Weak |
| Repeated Characters | `aaa` | Weak |
| Predictable Sequence | `abc123` | Weak |

### Test Case 1 — Strong Password

```text
Input: BlueTiger#47Moon

Result:
Strength: Strong
Common password: No
Predictable: No
```

### Test Case 2 — Medium Password

```text
Input: ghost123

Result:
Strength: Medium
```

### Test Case 3 — Weak Password

```text
Input: ghost

Result:
Strength: Weak

Suggestions:
- Use at least 8 characters
- Add an uppercase letter
- Add a number
- Add a special character
```

### Test Case 4 — Common Password

```text
Input: password123

Result:
Common password: Yes

Suggestion:
- Avoid common passwords
```

### Test Case 5 — Repeated Characters

```text
Input: aaa

Result:
Suggestion:
- Avoid repeating the same character
```

### Test Case 6 — Predictable Sequence

```text
Input: abc123

Result:
Suggestion:
- Avoid predictable sequences
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/mr-abhi-249/Password-Strength-Analyzer.git
```

### 2. Move into the project folder

```bash
cd Password-Strength-Analyzer
```

### 3. Run the program

```bash
python password_analyzer.py
```

## 💻 Example

```text
Enter password: BlueTiger#47Moon

Password Analysis
-----------------
Length           : 16
Uppercase        : Yes
Lowercase        : Yes
Number           : Yes
Special character: Yes
Common password  : No
Predictable      : No
Strength         : Strong
```

## 💡 Suggestions

The analyzer provides suggestions when security requirements are not met.

Examples:

```text
- Use at least 8 characters
- Add an uppercase letter
- Add a lowercase letter
- Add a number
- Add a special character
- Avoid common passwords
- Avoid predictable sequences
- Avoid repeating the same character
```

## 📚 What I Learned

- Python input handling
- Regular expressions
- Conditional statements
- Password validation
- Pattern detection
- Basic password-security concepts
- Git version control
- GitHub repository management
- Writing project documentation
- Testing different input conditions

## 📁 Project Structure

```text
Password-Strength-Analyzer/
│
├── password_analyzer.py
├── README.md
└── .gitignore
```

## 🎯 Project Information

**Challenge:** 21 Days 21 Projects  
**Day:** 1  
**Domain:** Cybersecurity  
**Project:** Password Strength Analyzer  
**Difficulty:** Beginner

## 🔮 Future Improvements

- Larger common-password database
- Password entropy calculation
- Secure password input without displaying characters
- GUI using Tkinter or Streamlit
- Breached-password checking using a suitable API

## 👨‍💻 Author

** Abhi Suguna kumar. Anaparthi **

Built as part of the **21 Days 21 Projects Challenge**.