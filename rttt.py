# simple banking system in python
balance = 10,000


def check_balance():
    print(f"your balance is : {balance}")
    initial_balance=int(input("input your initial bank balance: "))
    with open('ovo.txt', "w") as file:
        file.write(initial_balance)
        print(f"new initial balance is {initial_balance}")

def deposit():
    deposit= int(input("enter how much you want to deposit: "))
    new_balance=balance + deposit
    print(f"your new balance is: {new_balance}")

def withdraw():
    withdrawal=  int(input(f"how much do you want to withdraw : "))  
    if withdrawal <= balance:
        print(f"you have have withdrawn {withdrawal} ")
        after_withdrawal = balance - withdrawal
        print(f"new balance is {after_withdrawal}")
    elif withdrawal > balance:
        print(f"INSUFFICIENT BALANCE")
    else:
        print(f"INVALID WITHDRAWAL")
def log_out():
    print(f"ACCOUNT CLOSED!! ")
    
def main():
    print('select an option')
    print('1.check_balance')
    print('2.deposit')
    print('3.withdraw')
    print("4.log out")
try:
    choice =int(input("Enter your choice: "))

    if choice == 1:
            print(check_balance())
            main()
            
    elif choice == 2:
        print(deposit()) 
        main()
    elif choice == 3:
        print(withdraw())
    elif choice == 4:
        print(log_out())
    else:
        print("INVALID ENTRY")
except Exception as e:
    print(e)
finally:
    print("THANKS FOR USING THE PROGRAM!!")
        
main()





































#using sevral functions in python programming

# cars = ("range rover", "bmw", "jaguar")
# for index, value in enumerate(cars):
#     print(f"{index}:{value}")

# numbers = (1,2,3,4,5,555,55,55,55,55)
# print(numbers.index(5))




# a program that puts up random maths questions

# import random

# num1 = random.randint(3,12)
# num2 = random.randint(3,12)
# operators = ["+", "-", "*"]
# signs = random.choice(operators)



# def generate_problem():
#         expr = str(num1) +" " + signs + " " + str(num2)
#         answer = eval(expr)
#         return expr,answer


# expr,answer = generate_problem()
# print(expr,answer)

# import random

# def generate_problem():
#     num1 = random.randint(3, 12)
#     num2 = random.randint(3, 12)
#     operators = ["+", "-", "*"]
#     sign = random.choice(operators)
    
#     # Form the expression as a string
#     expr = f"{num1} {sign} {num2}"
    
#     # Calculate the answer using eval (safe since inputs are controlled)
#     answer = eval(expr)
    
#     return expr, answer

# # Generate and display a random math problem
# expr, answer = generate_problem()
# print(f"Question: {expr}")
# print(f"Answer: {answer}")






































# def intro(func):
#     def wrapper():
#         print('whats up you little fucker')
#         func()
#         print('am whats up liitle man')
#     return wrapper

# @intro
# def page_one():
#     print('say hello mr biggy ')
    

# page_one()
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()







    


# page_1()