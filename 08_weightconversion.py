# Python weight conversion

weight = float(input("Enter your weight: "))
unit = input("kilograms or pounds? (K or L): ")

if unit == "K" or "k":
    weight *= 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight,1)} {unit}")
elif unit == "L" or "l":
    weight /= 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight,1)} {unit}")
else:
    print(f"{unit} was not valid")

