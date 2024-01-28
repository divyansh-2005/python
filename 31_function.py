# def happy_birthday(name,age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age}!")
#     print("Happy birthday to you!")
#     print()

# happy_birthday("Divya", 19)
# happy_birthday("ayu", 20)
# happy_birthday("pihu", 20)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Divya", 450, "28/01/0204")


# def add(x,y):
#     z = x + y
#     return z

# def sub(x,y):
#     z = x - y
#     return z

# def mul(x,y):
#     z = x * y
#     return z

# def div(x,y):
#     z = x / y
#     return z

# print(add(1,2))
# print(sub(1,2))
# print(mul(1,2))
# print(div(1,2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Divya", "k")
print(full_name)