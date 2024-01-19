# name = input("Enter your name: ")

# if name == "":
#     print("you did not enter your name")
# else:
#     print(f"hello {name}")

# while name == "":
#    print("you did not enter your name")
#    name = input("Enter your name: ")

# print(f"hello {name}")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("age can't ne negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit)")

# while not food == "q":
#     print(f"you like {food}")
#     food = input("Enter a food you like (q to quit)")

# print("bye")

num = int(input("Enter a 3 betwen 1-10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a 3 betwen 1-10: "))

print(f"your number is {num}")