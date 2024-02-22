# You are going to write a program that will select a random name from a list of# names. The person selected will have to pay for everybody's food bill.

names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
random_index = random.randint(1, len(names))
random_name = names[random_index - 1]
print(f"{random_name} is going to buy the meal today!")

# another solution 
# random_index = random.randint(0, len(names) - 1)
# random_name = names[random_index]
