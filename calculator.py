#a calculator using class and methods 

class Math():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def divide(self):
        return self.num1 / self.num2
    def multiply(self):
        return self.num1 * self.num2
    
problem1 = Math(20,26)
print(problem1.multiply())