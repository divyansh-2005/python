# 1. default argument = A default value for certain parameters
#                       default is used when the argument is ommited
#                       make your function more flexible, reduce # of argument


# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1-discount) * (1+tax)

# print(net_price(500))
# print(net_price(500,0.1))
# print(net_price(500,0.1,0))


import time

def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(30,10)