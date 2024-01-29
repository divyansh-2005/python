class Car:

    wheels = 4 #class variable
        
    def __init__(self,make,model,year,color):
        self.make = make        #instanse variable
        self.model = model      #instanse variable
        self.year = year        #instanse variable
        self.color = color      #instanse variable

    def drive(self):
        print("This "+self.model+" car is driving")

    def stop(self):
        print("This "+self.model+" car is stopped")