import re

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty",
    "admin", "welcome", "letmein", "password123",
    "abc123", "111111", "123123"
}

SEQUENCES = [
    "123", "234", "345", "456", "567", "678", "789",
    "abc", "bcd", "cde", "def", "qwe", "wer", "ert"
]


def analyze_password(password):
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

    lower_password = password.lower()

    common = lower_password in COMMON_PASSWORDS
    predictable = any(sequence in lower_password for sequence in SEQUENCES)
    repeated = bool(re.search(r"(.)\1\1", password))

    if common:
        score -= 2
        suggestions.append("Avoid common passwords")

    if predictable:
        score -= 1
        suggestions.append("Avoid predictable sequences")

    if repeated:
        score -= 1
        suggestions.append("Avoid repeating the same character")

    score = max(0, score)

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "length": len(password),
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "number": bool(re.search(r"[0-9]", password)),
        "special": bool(re.search(r"[^A-Za-z0-9]", password)),
        "common": common,
        "predictable": predictable,
        "repeated": repeated,
        "score": score,
        "strength": strength,
        "suggestions": suggestions
    }