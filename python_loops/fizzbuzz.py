# Write your code here 👇
target = int(input("Enter a number between 0 and 100: \n"))
result = 0
for i in range(1, target + 1):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
