weight = int(input("Enter your weight: "))
unit = input("(L) lbs or (K) kilos: ")

if unit.upper() == "L":
    converted = round(weight * 0.45, 2)
    print(f"You are {converted} kilos ")

else:
    converted = round(weight / 0.45, 2)
    print(f"You are {converted} pounds")