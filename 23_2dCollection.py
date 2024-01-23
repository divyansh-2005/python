# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# print(groceries)
# print(groceries[0])
# print(groceries[1])
# print(groceries[2])
# print(groceries[0][0])
# print(groceries[1][0])
# print(groceries[1][1])

# groceries = [["apple", "orange", "banana", "coconut"],
#              ["celery", "carrots", "potatoes"],
#              ["chicken", "fish", "turkey"]]

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()


# Exercise - 2D keypad

num_pad = ((1,2,3,),
           (4,5,6),
           (7,8,9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()