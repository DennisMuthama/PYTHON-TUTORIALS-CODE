#enumarate().is used to give an index and value


colors = ('red', 'green', 'blue')

for i, color in enumerate(colors,start=10):
    print(f"{i}: {color}")
    
# count() – Returns the number of times an element appears in the tuple.
# my_tuple = (1, 2, 2, 3, 2)
# print(my_tuple.count(2))  # Output: 3


# index() – Returns the index of the first occurrence of an element.
# print(my_tuple.index(3))  # Output: 3
