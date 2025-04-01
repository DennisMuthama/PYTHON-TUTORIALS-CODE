user_input = input("Enter something to save in account.txt: ")

with open("account.txt", "w") as file:  # "w" mode overwrites the file
    file.write(user_input)

print("Data written to account.txt successfully.")





















class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class Manager(Person):
        def __init__(self, name, age,depa):
            super().__init__(name, age)
            self.depa = depa
            
        def salary(self):
            print(f"my salary is 10000000")
class Ceo(Person):
    def __init__(self,name,age,shares):
        super.__init__(name,age)
        self.shares = shares
        
    def salary(self):
        print("am paid in bitcoin")
    
manager =Manager("TATUM",23,"suppply")
print(manager.name)


    



# class Cars:
#     def __init__(self,name,age,pay) :
#         self.name = name
#         self.age = age
#         self.pay = pay
    
#     emp1 = Cars("dennis", "twenty", " five thousand")
        
    # def __str__(self,name,age,pay):
    #     return f" name: {name}, your age: {age}, pay:{pay}"
    





























#creating a class in python

# with open('ovo.txt') as file:
#     print(file.read())

# text= " T for trapster"

# with open('ovo.txt', 'a')as file:  << 'a' for append  w and r for read and write
#     file.write(text)












# try:   opening a file>>>>>>>>>
#     with open('c:\\Users\\Admin\\OneDrive\\Desktop\\dennis.txt') as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print(e)
#     print("you file has not be found")