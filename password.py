import re

def evaluate_password(pw):
    length = len(pw)
    score = 0
    # Length criterion
    if length >= 8:
        score += 1
    if re.search(r"[a-z]", pw): score += 1
    if re.search(r"[A-Z]", pw): score += 1
    if re.search(r"[0-9]", pw): score += 1
    if re.search(r"[^A-Za-z0-9]", pw): score += 1
    # Interpret score
    if score <= 2:
        return 'Weak'
    if score == 3 or score == 4:
        return 'Moderate'
    return 'Strong'

if __name__ == '__main__':
    pw = input("Enter password to evaluate: ")
    strength = evaluate_password(pw)
    print(f"Password Strength: {strength}")