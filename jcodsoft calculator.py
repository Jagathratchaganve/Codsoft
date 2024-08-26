def calculator():
    """A simple calculator that performs basic arithmetic operations."""

    print("Welcome to the Simple Calculator!")

    # Get user input for the two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Get user input for the operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation based on the chosen operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
        return

    # Display the result
    print("Result:", result)

# Call the calculator function
calculator()