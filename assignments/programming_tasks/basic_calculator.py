print("Welcome to basic Calculator program that performs basic arithmetic operations between two numbers.")
num1 = int(input("Please write a first number: "))
num2 = int(input("Please write a second number: "))
operator = input("Please specify the math operation here (+, -, *, /, %) : ")
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
else:
    print("Sorry, I can't understand your operation")
