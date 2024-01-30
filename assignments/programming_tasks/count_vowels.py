def countvowels(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char in vowels:
           count += 1
    return count
user_input = input("Write any word: ").lower()
result = countvowels(user_input.lower())
print(f"Number of vowels: {result}")
