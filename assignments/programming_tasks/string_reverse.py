def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

string = "Python"

print("The original string is : ", end="")
print(string)

print("The reversed string is : ", end="")
print(reverse(string))
