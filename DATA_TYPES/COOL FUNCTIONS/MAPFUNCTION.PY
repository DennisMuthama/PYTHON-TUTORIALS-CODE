# using the map function
# lamda is a single line function defined by the user

my_numbers = [1,2,3,12,5,6]
def my_squares(my_numbers):
    return my_numbers * my_numbers
    
squares=map(my_squares,my_numbers)
print(list(squares))

my_numbers = ["denni", "pull", "baddie"]

length=map(lambda x: x + "s",my_numbers)
print(list(length))

