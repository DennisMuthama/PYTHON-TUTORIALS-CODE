class Math:
    def __init__(self,number):
        self.number = number
        
    def addition(self,value):
        self.number += value
        return self.number
    
    def subtract(self,value):
        self.number -= value
        return self.number
    def __str__(self):
        return f"your answ is: {self.number}"
    
question1 = Math(20)
print(question1)
question1.subtract(5)
print(question1)





















































# class NumberPrinter:
#     def __init__(self, number):
#         self.number = number

#     def print_number(self):
#         print(f"The number is: {self.number}")

#     def add(self, value):
#         self.number += value
#         return self.number

#     def subtract(self, value):
#         self.number -= value
#         return self.number

#     def multiply(self, value):
#         self.number *= value
#         return self.number

#     def divide(self, value):
#         if value != 0:
#             self.number /= value
#             return self.number
#         else:
#             print("Error: Division by zero is not allowed.")
#             return None

#     def __str__(self):
#         return f"NumberPrinter with number: {self.number}"

# # Example usage:
# number_printer = NumberPrinter(10)
# number_printer.print_number()

# # Perform some operations
# number_printer.add(5)
# print(number_printer)  # Should print 15

# number_printer.subtract(3)
# print(number_printer)  # Should print 12

# number_printer.multiply(2)
# print(number_printer)  # Should print 24

# number_printer.divide(4)
# print(number_printer)  # Should print 6






# class Contant:
#     def __init__(self,name,number):
#         self.name = name
#         self.number = number
        
#     def display_details(self):
#         return f" name: {self.name} , your number:{self.number}"
    
# c1 = Contant('dennis', "0711205522")
# print(c1.display_details())