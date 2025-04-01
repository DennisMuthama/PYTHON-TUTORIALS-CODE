#they wrap a functiom and add functionality to that function 
#enable to add a greeting after the function is executed
#Decorators are functions that modify the behavior of other functions.
#Using functools.wraps is recommended to preserve the original function's metadata.
def my_wrapper(func):
    def wrapper():
        print("this is the before of the statement")
        func()
        print("this after the execution of the function")
    return wrapper

@my_wrapper
def say_hello():
    print("hello dennois the great one")
    
say_hello()
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called twice.")
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator()
# def say_hello():
#     print("Hello!")

# say_hello()
