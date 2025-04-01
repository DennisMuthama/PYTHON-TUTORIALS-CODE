#calling a function from the main function
def personal():
    print(f" my name is dennis")
def work():
    print(f" work at blockchains")
def education():
    print(f" studdy at crypto zombies")
    
def display():
    print(f"selection an option from below:")
    print(f"1.personal details:")
    print(f"2.work details:")
    print(f"3.education details")
    choice = input("choose an option")
    if choice =='1':
        personal()
    elif choice =='2':
        work()
    elif choice =='3':
        education()
    else:
        print(f"Enter a valid choice")

display()