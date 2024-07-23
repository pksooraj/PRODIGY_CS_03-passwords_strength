PINK = '\033[95m'
RESET = '\033[0m'
art = f"""{PINK}

_ \                                      |     __|  |                          |    |        __|  |                |              
  __/ _` | (_-< (_-< \ \  \ /  _ \   _| _` |   \__ \   _|   _| -_)    \    _` |   _|    \     (       \    -_)   _|  | /   -_)   _| 
 _| \__,_| ___/ ___/  \_/\_/ \___/ _| \__,_|   ____/ \__| _| \___| _| _| \__, | \__| _| _|   \___| _| _| \___| \__| _\_\ \___| _|  



{RESET}"""
import re
import math
import argparse
import getpass

def calculate_entropy(password):
    """Calculate the entropy of the given password."""
    pool = 0
    if re.search(r'[a-z]', password):
        pool += 26  # Lowercase letters
    if re.search(r'[A-Z]', password):
        pool += 26  # Uppercase letters
    if re.search(r'\d', password):
        pool += 10  # Digits
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        pool += 32  # Special characters (assuming a typical set)

    if pool == 0:
        return 0

    entropy = len(password) * math.log2(pool)
    return entropy

def evaluate_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    entropy_criteria = calculate_entropy(password) >= 50

    # Initialize feedback
    feedback = []
    score = 0

    # Evaluate criteria
    if length_criteria:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if lowercase_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if digit_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one numeric digit.")

    if special_char_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    if entropy_criteria:
        score += 1
    else:
        feedback.append("Password entropy is too low. Consider adding more unique characters.")

    # Determine strength
    if score == 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    
    parser = argparse.ArgumentParser(description='Password Strength Checker')
    parser.add_argument('-p', '--password', type=str, help='Password to check')
    args = parser.parse_args()

    if args.password:
        password = args.password
    else:
        print(art)
        password = getpass.getpass(prompt='Please enter a password: ')

    strength, feedback = evaluate_password_strength(password)

    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f" - {comment}")

if __name__ == "__main__":
    main()
