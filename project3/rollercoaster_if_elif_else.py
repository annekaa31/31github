print("Welcome to a rollercoaster!")
height = int(input("What is your height? "))
bill = 0
if height > 120:
  print("Congrats! You can ride the rollercoaster.")
  age = int(input("What's your age? "))
  if age < 12:
    bill = 5
    print(f"Your ticket price is ${bill}.")
  elif age <= 18:
    bill = 7
    print(f"Your ticket price is ${bill}.")
  elif age >= 45 and age <= 55:
    bill = 0
    print("The ticket is on us. No worries:)")
  else:
    bill = 12
    print(f"Your ticket price is ${bill}.")

  want_photo = input("Do you want a photo? Y or N: ")
  if want_photo == "Y":
    bill += 3
    print(f"Your final price is ${bill}")

else:
  print("Sorry, you have to grow taller to ride the rollercoaster.")
