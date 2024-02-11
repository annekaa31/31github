#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# My First solution

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))
result = float((((total_bill / total_people) * (tip / 100)) + (total_bill / total_people)))
rounded_result = round(result, 2)
print(f"Each person should pay: {rounded_result}")
print(type(rounded_result))


# My Second solution with more clean code
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))
bill_per_person = float((bill * (tip/100) + bill) / num_of_people)
rounded_total_bill = "{:.2f}".format(bill_per_person)
# rounded_total_bill = format(bill_per_person, ".2f")
# rounded_total_bill = round(bill_per_person, 2)
print(f"Each person should pay: {rounded_total_bill}")
