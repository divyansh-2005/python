# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# def func1():
#     a = 1
#     print(a)

# def func2():
#     b = 2
#     print(b)

# func1()
# func2()

from math import e

def func1():
    print(e)
    
e = 3

func1()