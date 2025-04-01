# a program to enumarate a to do list in python 

my_tasks = ["read a book", "wash dishes", "go out", "attend class", "Go home"]

for index,task in enumerate(my_tasks):
    print(f"{index + 1}. {task}")