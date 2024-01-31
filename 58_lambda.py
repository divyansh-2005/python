# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)

# lambda parameters:expression

# def double(x):
#     return x*2

# print(double(5))

double = lambda x:x*2
mul = lambda x, y: x*y
add = lambda x, y, z: x+y+z

age_check = lambda age:True if age >= 18 else False

print(double(5))
print(mul(3,5))
print(add(1,2,3))
print(age_check(12))