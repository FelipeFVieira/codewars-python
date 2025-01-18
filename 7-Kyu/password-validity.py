"""
Your job is to create a simple password validation function, as seen on many websites.

The rules for a valid password are as follows:

There needs to be at least 1 uppercase letter.
There needs to be at least 1 lowercase letter.
There needs to be at least 1 number.
The password needs to be at least 8 characters long.
You are permitted to use any methods to validate the password.

Kata Level: 7 Kyu

Link: https://www.codewars.com/kata/56a921fa8c5167d8e7000053
"""

def password_validity(password):
    # Check the length of the password
    if len(password) < 8:
        return False

    # Initialize flags for each condition
    has_upper = False
    has_lower = False
    has_digit = False

    # Check each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    # Return True if all conditions are met
    return has_upper and has_lower and has_digit

# Test cases
print(password_validity("Abcd1234"))  # True
print(password_validity("Abcd123"))   # False
print(password_validity("abcd1234"))  # False
print(password_validity("AbcdefGhijKlmnopQRsTuvwxyZ1234567890"))  # True
print(password_validity("ABCD1234"))  # False
print(password_validity("Ab1!@#$%^&*()-_+={}[]|\\:;?/>.<,"))  # True
print(password_validity("!@#$%^&*()-_+={}[]|\\:;?/>.<,"))  # False
