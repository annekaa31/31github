print("Welcome to a rollercoaster!")
height = int(input("What is your height? "))
if height > 120:
  print("Congrats! You can ride the rollercoaster.")
  age = int(input("What's your age? "))
  if age < 12:
    print("Your ticket price is $5.")
  elif age <= 18:
    print("Your ticket price is $7.")
  else:
    print("Your ticket price is $12.")
else:
  print("Sorry, you have to grow taller to ride the rollercoaster.")
