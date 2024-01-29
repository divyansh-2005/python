from car import Car

# class Car:
    
#     def __init__(self,make,model,year,color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color

#     def drive(self):
#         print("This "+self.model+" car is driving")

#     def stop(self):
#         print("This "+self.model+" car is stopped")


# Main class
        
car1 = Car("chevy","Corvette",2011,"blue")
car2 = Car("Ford","Mustang",2022,"red")

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)

car1.drive()
car1.stop()

print()

print(car2.make)
print(car2.model)
print(car2.year)
print(car2.color)

car2.drive()
car2.stop()