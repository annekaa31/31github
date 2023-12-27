print("Welcome to basic Calculator program that performs basic arithmetic operations between two numbers.")
num1 = int(input("Please write a first number: "))
num2 = int(input("Please write a second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = round(num1 / num2, 2)
print(f"The addition is: {addition}, the subtraction is: {subtraction}, the multiplication is: {multiplication}, the division is: {division}")
