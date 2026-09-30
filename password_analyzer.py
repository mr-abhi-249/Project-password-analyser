import re

password = input("Enter password: ")

score = 0
suggestions = []

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

if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("\nPassword Analysis")
print("-----------------")
print(f"Length          : {len(password)}")
print(f"Uppercase       : {'Yes' if re.search(r'[A-Z]', password) else 'No'}")
print(f"Lowercase       : {'Yes' if re.search(r'[a-z]', password) else 'No'}")
print(f"Number          : {'Yes' if re.search(r'[0-9]', password) else 'No'}")
print(f"Special character: {'Yes' if re.search(r'[^A-Za-z0-9]', password) else 'No'}")
print(f"Strength        : {strength}")

if suggestions:
    print("\nSuggestions")
    for suggestion in suggestions:
        print(f"- {suggestion}")