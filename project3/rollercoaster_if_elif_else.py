print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))
if height >= 120:
  print("Congrats! You can ride a rollercoaster.")
  age = int(input("What's your age? "))
  if age < 12:
    print("Your ticket price is $5.")
  elif age <= 18:
    print("Your ticket prace is $7.")
  else:
    print("Your ticket prace is $12.")
else:
  print("Sorry, you havee to grow taller to ride a rollercoaster.")
