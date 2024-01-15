#what Jordan taught
print("HELLO")

def add(num1, num2):
    return num1 + num2
 
def subtract(num1, num2):
    return num1 - num2
 
def multiply(num1, num2):
    return num1 * num2
 
def divide(num1, num2):
    if num2 == 0:
        return "Error: Can't divide by zero"
    else:
        return num1 / num2
 
def calculator():
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
 
    choice = input()
 
    if choice == "1":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print(add(num1, num2))
 
    if choice == "2":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print(subtract(num1, num2))

    if choice == "3":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print(multiply(num1, num2))

    if choice == "4":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print(divide(num1, num2))

calculator()



#chat gpt creates
def calculator():
    operation = input("Enter operation (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

    return f"Result: {num1} {operation} {num2} = {result}"

# Test the calculator function
print(calculator())