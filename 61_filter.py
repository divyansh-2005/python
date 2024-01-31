# filter() = creates a collection of elements from an iterable for which a function returns ture

# filter(function, iterable)/

friends = [("ayush",19),
           ("ansh",21),
           ("piyush",20),
           ("kamla",29)]

age = lambda data:data[1] > 20

new_friends = list(filter(age, friends))

for i in new_friends:
    print(i)
