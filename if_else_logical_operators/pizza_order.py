print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
pizza_price = 0
if size == "S":
  pizza_price += 15
  if add_pepperoni == "Y":
    pizza_price += 2
  else:
    pizza_price
  if extra_cheese == "Y":
    pizza_price +=1
  else:
    pizza_price
  print(f"Your final bill is: ${pizza_price}.")
# print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: ${pizza_price}.")
if size == "M":
  pizza_price += 20
  if add_pepperoni == "Y":
    pizza_price +=3
  else:
    pizza_price
  if extra_cheese == "Y":
    pizza_price +=1
  else:
    pizza_price
  print(f"Your final bill is: ${pizza_price}.")
if size == "L":
  pizza_price += 25
  if add_pepperoni == "Y":
    pizza_price += 3
  else: 
    pizza_price
  if extra_cheese == "Y":
    pizza_price += 1
  else:
    pizza_price
  print(f"Your final bill is: ${pizza_price}.")


# Another yet solution

# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# elif size == "L":
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3

# if extra_cheese == "Y":
#   bill +=1

# print(f"Your final bill is: ${bill}.")
