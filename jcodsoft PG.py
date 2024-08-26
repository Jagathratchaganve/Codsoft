import random
import string

def generate_password(length):
    # Define the character set: lowercase, uppercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    while True:
        # Prompt the user to specify the desired length of the password
        while True:
            try:
                length = int(input("Enter the desired length of the password: "))
                if length < 1:
                    print("Please enter a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")
        
        # Ask if the user wants to generate another password
        repeat = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
