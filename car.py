class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model = model
        self.year = year
    def move(self):
        print("this car is moving")
    
    def stop(self):
            print("this car is stopping")