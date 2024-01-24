# Define a function f(n) such that f(n) = n * f(n-1) with f(1) = 1. What is f(5)?

def f(n):
    if n == 1:
        return 1
    else:
        # f(n) = n * f(n-1)
        return n * f(n - 1)

result = f(5)
print(result)
