def f(n):
    if n == 1:
        return 1
    else:
        # f(n) = n * f(n-1)
        return n * f(n - 1)

n = int(input("This program calculates the factorial of a given number. Please write a number: "))
result = f(n)
print(result)
