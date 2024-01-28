# 3.Arbitrary meaing varring
# *args = allows you to pass multiple non-key argument (type = tuple)
# **kwargs = allows you to pass multiple keyword-argument (type = dictionary)
#           * unpacking operator

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1,2,3))

# def display_anme(*args):
#     print(type(args))
#     for arg in args:
#         print(arg, end=" ")

# display_anme("divya", "k", "IIT")


# def print_address(**kwargs):
#     print(type(kwargs))
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")

# print_address(street="123 fake St.",
#               city= "Nagpur",
#               state= "Maha",
#               zip="465412")


# EXERCISE
def shipping_lable(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    # for value in kwargs.values():
    #     print(value,end=" ")

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_lable("Ms.", "pihu", "D." ,"19",
               street="123 fake St.",
               city= "Nagpur",
            #    apt="#101",
               state= "Maha",
               zip="465412")