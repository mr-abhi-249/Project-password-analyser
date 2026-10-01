import re

password = input("Enter password: ")

score = 0
suggestions = []

common_passwords = {
    "password", "123456", "12345678", "qwerty",
    "admin", "welcome", "letmein", "password123",
    "abc123", "111111", "123123"
}

sequences = [
    "123", "234", "345", "456", "567", "678", "789",
    "abc", "bcd", "cde", "def", "qwe", "wer", "ert"
]

if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters")

if re.search(r"[A-Z]", password):
    score += 1
else:
    suggestions.append("Add an uppercase letter")

if re.search(r"[a-z]", password):
    score += 1
else:
    suggestions.append("Add a lowercase letter")

if re.search(r"[0-9]", password):
    score += 1
else:
    suggestions.append("Add a number")

if re.search(r"[^A-Za-z0-9]", password):
    score += 1
else:
    suggestions.append("Add a special character")

lower_password = password.lower()

if lower_password in common_passwords:
    score -= 2
    suggestions.append("Avoid common passwords")

if any(sequence in lower_password for sequence in sequences):
    score -= 1
    suggestions.append("Avoid predictable sequences")

if re.search(r"(.)\1\1", password):
    score -= 1
    suggestions.append("Avoid repeating the same character")

score = max(0, score)

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("\nPassword Analysis")
print("-----------------")
print(f"Length           : {len(password)}")
print(f"Uppercase        : {'Yes' if re.search(r'[A-Z]', password) else 'No'}")
print(f"Lowercase        : {'Yes' if re.search(r'[a-z]', password) else 'No'}")
print(f"Number           : {'Yes' if re.search(r'[0-9]', password) else 'No'}")
print(f"Special character: {'Yes' if re.search(r'[^A-Za-z0-9]', password) else 'No'}")
print(f"Common password  : {'Yes' if lower_password in common_passwords else 'No'}")
print(f"Predictable      : {'Yes' if any(s in lower_password for s in sequences) else 'No'}")
print(f"Strength         : {strength}")

if suggestions:
    print("\nSuggestions")
    for suggestion in suggestions:
        print(f"- {suggestion}")