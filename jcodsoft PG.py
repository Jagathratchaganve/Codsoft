import random
import string

def generate_password(length, complexity):
    """Creates a strong, random password of the specified length and complexity.

    Args:
        length: The desired length of the password.
        complexity: The desired complexity of the password (1 for simple, 2 for medium, 3 for strong).

    Returns:
        The generated password.
    """

    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Please choose 1, 2, or 3.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    desired_length = int(input("How long would you like your password to be? "))
    desired_complexity = int(input("Choose the password complexity (1 for simple, 2 for medium, 3 for strong): "))
    generated_password = generate_password(desired_length, desired_complexity)
    print("Your new password is:", generated_password)