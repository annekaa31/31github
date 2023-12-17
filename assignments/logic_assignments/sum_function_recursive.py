def sum_n(n):
    if n == 1:
        return 1
    else:
        #sum_n(n) = sum_n(n - 1) + n
        return sum_n(n - 1) + n

result = sum_n(100)
print(result)
