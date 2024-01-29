from car import Car

# class Car:

#     wheels = 4 #class variable
        
#     def __init__(self,make,model,year,color):
#         self.make = make        #instanse variable
#         self.model = model      #instanse variable
#         self.year = year        #instanse variable
#         self.color = color      #instanse variable

car1 = Car("chevy","Corvette",2011,"blue")
car2 = Car("Ford","Mustang",2022,"red")

# car1.wheels = 2
Car.wheels = 2

print(car1.wheels)
print(car2.wheels)

# print(Car.wheels)