def calculator():
    while True:
        operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")
        if operation == 'q':
            break
        if operation in ('+', '-', '*', '/'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if operation == '+':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif operation == '-':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif operation == '*':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif operation == '/':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Cannot divide by zero")
        else:
            print("Invalid operation")

if __name__ == "__main__":
    calculator()
