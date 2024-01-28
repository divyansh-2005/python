# dictionary = a collection of {key:value} pairs 
#              ordered and changable. No duplicates

capitals = {"USA":"Washington D.C",
            "India": "New Delhi",
            "China": "Beiging",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))


print(capitals.get("India"))
# print(capitals.get("Japan"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exists")


# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Detorit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()

# for key in capitals.keys():
#     print(key)

# values = capitals.values()

# for value in capitals.values():
#     print(value)

# items = capitals.items()
# for key,value in capitals.items():
#     print(f"{key}: {value}")