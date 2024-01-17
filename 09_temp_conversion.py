unit = input("celsius or fahrenheit (C/F): ")
temp = float(input("Enter temp.: "))

if unit == "C":
    temp = round((9*temp)/ 5+32, 1)
    print(f"Temp in F is: {temp}F")
elif unit == "F":
    temp = round((temp-32) * 5/9, 1)
    print(f"Temp in C is: {temp}C")
else: 
    print(f"{unit} is an invalid unit")