#nested loops in python

rows = int(input('Enter the number of rows: '))
columns = int(input('Enter the number of columns: '))
symbol = input('enter the symbol to use ')

for row in range(rows):
    print(row)
    for column in range(columns):
        print(symbol)
    




#creating a list from a range
# for x in range(3):
#     print('i like food')

# numbers = list(range(1,11))   
# print(numbers)

# for i in range(10):
#     print("Iteration")


# for x in range(0,10,2):
#     print(x)