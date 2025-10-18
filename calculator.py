# --------------------------------------------------------------
# Title   : Basic Calculator with Error Handling
# Author  : (Your Name)
# Date    : (Enter Date)
# Purpose : To perform basic arithmetic operations with error handling
# --------------------------------------------------------------

# ===== Calculator Functions =====
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def power(a, b):
    return a ** b


# ===== Helper Function for Input Validation =====
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# ===== Perform the Calculation =====
def perform_calculation(choice):
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    if choice == '1':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"Result: {num1} / {num2} = {result}")
    elif choice == '5':
        result = power(num1, num2)
        print(f"Result: {num1} ^ {num2} = {result}")
    else:
        print("Invalid operation!")


# ===== Main Program =====
def calculator():
    print("===================================")
    print("   BASIC CALCULATOR WITH ERRORS    ")
    print("===================================")

    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '6':
            print("\nExiting calculator. Goodbye!")
            break
        elif choice in ['1', '2', '3', '4', '5']:
            perform_calculation(choice)
            
            # Ask if user wants to continue
            while True:
                cont = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
                if cont == 'y':
                    break  # Continue to menu
                elif cont == 'n':
                    print("\nThank you for using the calculator. Goodbye!")
                    return  # Exit the program
                else:
                    print("Invalid input! Please enter 'y' or 'n'.")
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


# ===== Run the Calculator =====
if __name__ == "__main__":
    calculator()
