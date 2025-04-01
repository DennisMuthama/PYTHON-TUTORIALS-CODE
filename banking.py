import os

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
        else:
            print(f"Invalid withdrawal amount. Maximum you can withdraw is ${self.balance}")


    def display_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: ${self.balance}")


def save_account(account):
    with open(f"{account.account_holder}.txt", "w") as file:
        file.write(f"{account.account_holder},{account.balance}")
    print("Account data saved successfully.\n")

def load_account(account_holder):
    if os.path.exists(f"{account_holder}.txt"):
        with open(f"{account_holder}.txt", "r") as file:
            data = file.read().split(",")
            return BankAccount(data[0], float(data[1]))
    else:
        print("No account found with that name.")
        return None


def create_account():
    name = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial deposit amount: "))
    account = BankAccount(name, initial_balance)
    print(f"Account created for {name} with balance ${initial_balance}.\n")
    return account


def main():
    account = None

    while True:
        print("\nBank Account Menu:")
        print("1. Create New Account")
        print("2. Load Existing Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Display Balance")
        print("6. Save Account")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            account = create_account()
        elif choice == "2":
            name = input("Enter account holder's name: ")
            account = load_account(name)
        elif choice == "3":
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("No account loaded. Please create or load an account first.")
        elif choice == "4":
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("No account loaded. Please create or load an account first.")
        elif choice == "5":
            if account:
                account.display_balance()
            else:
                print("No account loaded. Please create or load an account first.")
        elif choice == "6":
            if account:
                save_account(account)
            else:
                print("No account loaded. Please create or load an account first.")
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")


main()
