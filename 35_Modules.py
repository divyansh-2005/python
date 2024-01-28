# module = a file containg code ypu want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program resuable separate files

# print(help("modules"))

# import math
# import math as math
# from math import pi

import exampleModule

result = exampleModule.pi
result = exampleModule.square(3)
result = exampleModule.cube(3)
result = exampleModule.area(3)

print(result)
