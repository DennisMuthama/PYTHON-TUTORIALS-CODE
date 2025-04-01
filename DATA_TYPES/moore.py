# a to do list in python

def add_task():
    task = input("ENTER THE TASK TO ADD:")
    print(f"you added {task}")

def view_tasks():
    with open("ovo.txt", "r") as file:
        print(file.read)
    

def save_tasks():
    with open("ovo.txt", "w") as file:
        file.write(add_task())
    
def delete_tasks():
    with open("ovo.txt", "a") as file:
        file.write(add_task())

def  main():
    print('select an option below \n')
    print('1.ADD TASK')
    print('2.VIEW TASKS \n')
    print('3.DELETE TASKS \n')
    print("4.SAVE TASKS")
try:
    choice=int(input("Select an option: ")) 
    if choice == 1:
        add_task()
    elif choice == 2:
       view_tasks()
    elif choice == 3:
       save_tasks()
    elif choice == 4:
       delete_tasks()
    else:
        print(f"INVALID OUTPUT")
except Exception as e:
    print(e)

finally:
    print("THANKS FOR USING THIS PROGRAM")

main()