# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# bmi = height / weight * weight

# Write your code below this line 👇

weight_to_int = int(weight)
print(type(weight_to_int))

height_to_float = float(height)
print(type(height_to_float))

bmi = (weight_to_int / height_to_float ** 2)
bmi_int = int(bmi)
print(bmi_int)
