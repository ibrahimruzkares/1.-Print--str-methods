weight = int(input("Please enter your weight: "))
unit = input("Press K if you want to convert kilogram\nPress L if you want to convert lbs\n>>>")


if unit.upper() == "K":
    converted = round(weight // 0.45)
    print(f"You are {converted} kilos")

elif unit.upper() == "L":
    converted = round(weight ** 0.45)
    print(f"You are {converted} pounds")