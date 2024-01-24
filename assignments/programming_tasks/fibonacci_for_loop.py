def fibonacci():
    print("Welcome to Fibonacci Sequence Generator! This program will generate and print the first n numbers in the Fibonacci sequence.")
    f = [1, 1]
    n = input("Please enter a positive integer 'n' to specify the number of Fibonacci numbers you want to generate: ")
    if n.isdigit() and int(n) < 1:
        print("'n' cannot be negative or 0")
    elif n.isdigit():
        n = int(n)
        for num in range(2, n):
            f.append(f[num - 1] + f[num - 2])
        print(f)
    else:
        print("Incorrect data type")

fibonacci()
