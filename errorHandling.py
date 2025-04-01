# a simple program to divide the numerator and denominator
# the try put all the user input under this function as you dont kniw what the user will input
#create exeptions starting with specific ones then put a general one at the end
# thhe finally ppart always executes irregardless

try:
    numerator=int(input("enter the numerator: "))
    denominator = int(input("enter the denominator: "))
    result= numerator/denominator
    print(result)
except ZeroDivisionError as e:
        print(e)
        print("you cant divide the number by zero")
except ValueError as e:
    print(e)
    print("enter a valid number ")
except Exception as e:
    print(e)
    print("invalid response ")
finally:
    print("this will always execute")