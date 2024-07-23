
# Password Strength Checker

This Python script evaluates the strength of a given password based on multiple criteria including length, character variety, and entropy. The script provides feedback to help improve the password's security.

## Features

- Checks password against the following criteria:
  - Minimum length of 8 characters
  - Inclusion of at least one uppercase letter
  - Inclusion of at least one lowercase letter
  - Inclusion of at least one numeric digit
  - Inclusion of at least one special character
  - Minimum entropy of 50 bits
- Provides a score and feedback on how to improve the password strength.

## Requirements

- Python 3.x

## Usage

You can use the script by providing a password as a command-line argument or by entering it interactively when prompted.

### Command Line Argument

To check a password provided as a command-line argument, use the `-p` or `--password` option:

```sh
python password_strength_checker.py -p YourPasswordHere
```

### Interactive Mode

If you do not provide a password as a command-line argument, the script will prompt you to enter a password interactively:

```sh
python password_checker.py
```

## Example Output

### Strong Password

```sh
$ python password_checker.py -p StrongP@ssw0rd!
Password Strength: Strong
```

### Weak Password with Feedback

```sh
$ python password_checker.py -p weak
Password Strength: Weak
Feedback:
 - Password should be at least 8 characters long.
 - Password should include at least one uppercase letter.
 - Password should include at least one special character.
 - Password entropy is too low. Consider adding more unique characters.
```

## Script Details

### Functions

- `calculate_entropy(password)`: Calculates the entropy of the given password based on character pool.
- `evaluate_password_strength(password)`: Evaluates the password strength based on predefined criteria and provides feedback.
- `main()`: Handles command-line arguments and prompts user for password input.

### Criteria for Evaluation

1. **Length**: Password should be at least 8 characters long.
2. **Uppercase Letter**: Password should include at least one uppercase letter.
3. **Lowercase Letter**: Password should include at least one lowercase letter.
4. **Numeric Digit**: Password should include at least one numeric digit.
5. **Special Character**: Password should include at least one special character.
6. **Entropy**: Password entropy should be at least 50 bits.

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue.

---

Feel free to adjust the content as per your specific needs.
