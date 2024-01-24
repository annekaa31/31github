print("Welcome to basic Calculator program that performs basic arithmetic operations between two numbers.")
num1 = int(input("Please write a first number: "))
if num1.isdigit():
    num1 = int(num1)
else:
    print("Incorrect user input")
operator = input("Please specify the math operation here (+, -, *, /, %) : ")
num2 = int(input("Please write a second number: "))
if num2.isdigit():
    num2 = int(num2)
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = round(num1 / num2, 2)
    if operator == "+":
        print(f"{num1} + {num2} = {addition}")
    elif operator == "-":
        print(f"{num1} - {num2} = {subtraction}")
    elif operator == "*":
        print(f"{num1} * {num2} = {multiplication}")
    elif operator == "/":
        print(f"{num1} / {num2} = {division}")
