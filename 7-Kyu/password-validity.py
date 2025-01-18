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
