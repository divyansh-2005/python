# Python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("principle can't be negative")
    else:
        break

while True:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print("rate can't be negative")
    else:
        break

while True:
    time = int(input("Enter the time amount: "))
    if time <= 0:
        print("time can't be negative")
    else:
        break
    
total = principle * pow((1+ rate / 100),time)

print(f"Balance after {time} year/s: ${total:.2f}")