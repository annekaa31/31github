print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
couple_name = name1.lower() + name2.lower()

t = couple_name.count("t")
r = couple_name.count("r")
u = couple_name.count("u")
e = couple_name.count("e")
total1 = t + r + u + e 

l = couple_name.count("l")
o = couple_name.count("o")
v = couple_name.count("v")
e = couple_name.count("e")
total2 = l + o + v + e 
love_score = int(str(total1) + str(total2))

if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
