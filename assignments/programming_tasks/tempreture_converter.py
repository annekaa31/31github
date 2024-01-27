temperature = input("Write temperature that you want to convert: ")
# a = temperature[len(temperature)-1]
# print(a)
if temperature[len(temperature)-1] == "f":
    temperature = int(temperature.rstrip(temperature[-1]))
    result = round(5/9 * (temperature - 32))
    print(f"{result} celsius")
elif temperature[len(temperature)-1] == "c":
    temperature = int(temperature.rstrip(temperature[-1]))
    # print(temperature)
    result = round(temperature * (9/5) + 32)
    print(f"{result} fahrenheit")
