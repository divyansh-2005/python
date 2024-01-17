# name = input("Enter your full name: ")
# phone_number = input("Enter your phone no: ")

# result = len(name)
# result = name.find("a")
# result = name.rfind("a")
# result = name.rfind("z")
# name = name.capitalize()  #only first letter
# name = name.upper()
# name = name.lower()
# name = name.isdigit()
# name = name.isalpha()

# result = phone_number.count("-")
# phone_number = phone_number.replace("-", "")

# print(phone_number)

# print(help(str))


#exercise 
username = input("Enter user name: ")
len = len(username)
space = username.find(" ")
digit = username.isalpha()

if len > 12:
    print(f"{len} is greater than 12 characters")
elif space != -1:
    print(f"{username} contains space")
elif digit == False:
    print(f"{username} conatins digits")
else:
    print("Everything is alright")
