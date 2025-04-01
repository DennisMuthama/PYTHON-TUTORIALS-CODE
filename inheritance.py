# creating abastract classes

# creating a super function in python

# class Rectangele:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

# class Square(Rectangele):
#     def __init__(self,length,width):
#         super(). __init__(length,width)
        
#     def area(self):
#         return self.length * self.width

# class Cube(Rectangele):
#     def __init__(self,length,width,height):
#         super().__init__(length,width)
#         self.height = height
        
#     def volume(self):
#         return self.length * self.width * self.height

# square1 = Square(2,5)
# cube1=Cube(2,7,10)

# print(cube1.volume())
# print(square1.area())
#inheritance in py to craete a recatangle,cube

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def volume(self):
        return self.length * self.width * self.height
    
cube1 = Cube(10,20,30)
print(cube1)

rect1=Rectangle(90,10)
answ = rect1.area()
print(f"the area of the rectangle is {answ}")




























# class Vehicle:
#     alive = True
#     def move(self):
#             print('this car is moving ')
        
#     def brake(self):
#             print('this car is braking')
            
#     def speeding(self):
#             print('this car is speeding ')

# class BMW(Vehicle):
#         pass
    
# class AUDI(Vehicle):
#         pass
    
# class Benz(Vehicle):
#         pass
    
# bmw=BMW()
    
# bmw.move()