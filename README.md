# 🔐 Password Strength Analyzer

A web-based cybersecurity mini project that analyzes password strength using character validation, common-password detection, predictable-pattern detection, and repeated-character detection.

The project uses **Python + Flask** for the backend and **HTML, CSS, and JavaScript** for the frontend.

---

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
- Shows password strength meter
- Displays security checklist
- Show/Hide password
- Press Enter to analyze password
- Responsive web interface
- Flask REST API backend

---

## 🛠️ Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python 3
- Flask
- Regular Expressions (`re`)

### Tools

- Git
- GitHub
- VS Code

---

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

### Application Flow

```text
User
  ↓
Frontend
HTML + CSS + JavaScript
  ↓
POST /api/analyze
  ↓
Flask Backend
  ↓
Password Analyzer
  ↓
JSON Result
  ↓
Frontend
  ↓
Strength + Checklist + Suggestions
```

---

## 🧪 Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| Strong Password | `BlueTiger#47Moon` | Strong |
| Medium Password | `Ghost123` | Medium |
| Weak Password | `ghost` | Weak |
| Common Password | `password123` | Weak |
| Repeated Characters | `aaa` | Weak |
| Predictable Sequence | `abc123` | Weak |

> These are demonstration passwords only. Do not use them as real passwords.

---

## 🧪 Test Case 1 — Strong Password

```text
Input: BlueTiger#47Moon

Result:
Strength: Strong
Common password: No
Predictable: No
```

---

## 🧪 Test Case 2 — Medium Password

```text
Input: Ghost123

Result:
Strength: Medium
```

---

## 🧪 Test Case 3 — Weak Password

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

---

## 🧪 Test Case 4 — Common Password

```text
Input: password123

Result:
Common password: Yes

Suggestion:
- Avoid common passwords
```

---

## 🧪 Test Case 5 — Repeated Characters

```text
Input: aaa

Result:
Suggestion:
- Avoid repeating the same character
```

---

## 🧪 Test Case 6 — Predictable Sequence

```text
Input: abc123

Result:
Suggestion:
- Avoid predictable sequences
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/mr-abhi-249/Password-Strength-Analyzer.git
```

### 2. Move into the project folder

```bash
cd Password-Strength-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Flask application

```bash
python backend/app.py
```

### 7. Open the website

```text
http://127.0.0.1:5000/
```

---

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

The same analysis is also displayed through the web interface with a visual strength meter, checklist, and suggestions.

---

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

---

## 📸 Screenshots

Screenshots of the web application are stored in the `screenshots/` folder.

Example:

```text
screenshots/
├── weak.png
├── medium.png
└── strong.png
```

You can display them here:

```markdown
### Strong Password

![Strong Password](screenshots/strong.png)

### Medium Password

![Medium Password](screenshots/medium.png)

### Weak Password

![Weak Password](screenshots/weak.png)
```

---

## 📚 What I Learned

- Python input handling
- Regular expressions
- Conditional statements
- Password validation
- Pattern detection
- Basic password-security concepts
- Flask backend development
- REST API basics
- JSON communication
- JavaScript Fetch API
- Frontend-backend communication
- HTML/CSS web development
- Git version control
- GitHub repository management
- Writing project documentation
- Testing different input conditions

---

## 📁 Project Structure

```text
Password-Strength-Analyzer/
│
├── backend/
│   ├── app.py
│   └── analyzer.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── screenshots/
│   ├── weak.png
│   ├── medium.png
│   └── strong.png
│
├── password_analyzer.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🎯 Project Information

**Challenge:** 21 Days 21 Projects

**Day:** 1

**Domain:** Cybersecurity + Python + Web Development

**Project:** Password Strength Analyzer

**Difficulty:** Beginner

---

## 🔮 Future Improvements

- Larger common-password database
- Password entropy calculation
- More advanced password scoring
- Password generator
- Breached-password checking using a suitable API
- Improved UI animations
- Dark/light theme
- Deployment as a public web application

---

## 🔒 Security Note

This project does not intentionally store or log passwords entered by the user.

For demonstration purposes, use dummy passwords rather than real passwords.

---

## 👨‍💻 Author

**Abhi Suguna Kumar Anaparthi**

Built as part of the **21 Days 21 Projects Challenge**.
```

```bash
python backend/app.py
```
