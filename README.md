# 🔐 Password Strength Analyzer

A Python-based cybersecurity mini project that analyzes password strength
using character validation, common-password detection, and predictable-pattern detection.

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

## 🧪 Example

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

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/mr-abhi-249/Project-password-analyser-.git