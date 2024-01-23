# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unorederd and immntable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("apple", "orange", "banana", "coconut", "coconut")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

print(fruits.index("apple"))
print(fruits.count("coconut"))

print(fruits)
# print(fruits[0:3])
# print(fruits[::2])
# print(fruits[::-1])

# for fruit in fruits:
#     print(fruit)