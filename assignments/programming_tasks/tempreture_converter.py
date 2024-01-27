temperature = input("Write temperature that you want to convert: ")
# print(temperature[0])
# print(temperature[1])
# print(temperature[2])
# print(temperature[len(temperature) - 1])
if temperature[len(temperature) - 1] == "f" or temperature[len(temperature) - 1] == "F":
    temperature = int(temperature.rstrip(temperature[-1]))
    result = round(5 / 9 * (temperature - 32))
    print(f"{result} celsius")
elif temperature[len(temperature) - 1] == "c" or temperature[len(temperature) - 1] == "C":
    temperature = int(temperature.rstrip(temperature[-1]))
    result = round(temperature * (9 / 5) + 32)
    print(f"{result} fahrenheit")
else:
    print("Incorrect user input")
