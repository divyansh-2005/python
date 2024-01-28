# 2.keyword argument = an argument preceded by an identifier
#                    helps with readbility
#                    order of arguments doesn't matter


# def hello(greeting,title,first,last):
#     print(f"{greeting} {title}{first} {last}")

# hello("Hello", "Mr.", "K", "Divya")
# hello("Hello", title="Mr.", last="K",first="Divya")

# for x in range(1,11):
#     print(x, end=" ")

# print("1", "2", "3", "4", "5", sep="-")


# EXERCISE
def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"    

phone_num = get_phone(country=91, area=123, first=546, last=7890)
print(phone_num)