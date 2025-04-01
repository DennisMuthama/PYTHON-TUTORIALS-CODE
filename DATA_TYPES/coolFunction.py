import json

# Function to read data from JSON
def read_json(filename="users.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to write data to JSON
def write_json(data, filename="users.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Function to get user input
def get_user_input(prompt, validator=None):
    while True:
        user_input = input(prompt)
        if validator and not validator(user_input):
            print("Invalid input. Please try again.")
        else:
            return user_input

# Validator for phone number (must be 10 digits)
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

# Function to register a new user
def register_user():
    print("\n--- User Registration ---")
    full_name = get_user_input("Enter your full name: ")
    phone_number = get_user_input("Enter your phone number (10 digits): ", is_valid_phone)
    balance = get_user_input("Enter your balance: ", lambda x: x.replace('.', '', 1).isdigit())

    user_data = {
        "full_name": full_name,
        "phone_number": phone_number,
        "balance": float(balance)  # Convert balance to float
    }

    users = read_json()
    users.append(user_data)
    write_json(users)

    print(f"\n✅ User {full_name} registered successfully!\n")

# Function to display all users
def display_users():
    users = read_json()
    if not users:
        print("\n❌ No users found.\n")
        return

    print("\n--- User List ---")
    for user in users:
        print(f"👤 Name: {user['full_name']}, 📞 Phone: {user['phone_number']}, 💰 Balance: ${user['balance']}")
    print()

# Function to find a user by phone number
def find_user():
    phone_number = get_user_input("Enter phone number to search: ", is_valid_phone)
    users = read_json()
    
    for user in users:
        if user["phone_number"] == phone_number:
            print(f"\n🔍 User Found: {user['full_name']} | 💰 Balance: ${user['balance']}\n")
            return

    print("\n❌ User not found.\n")

# Function to delete a user
def delete_user():
    phone_number = get_user_input("Enter phone number to delete: ", is_valid_phone)
    users = read_json()
    updated_users = [user for user in users if user["phone_number"] != phone_number]

    if len(users) == len(updated_users):
        print("\n❌ User not found.\n")
    else:
        write_json(updated_users)
        print("\n✅ User deleted successfully!\n")

# Function to display menu and interact with user
def main():
    while True:
        print("\n📌 Choose an option:")
        print("1️⃣ Register User")
        print("2️⃣ Display Users")
        print("3️⃣ Find User")
        print("4️⃣ Delete User")
        print("5️⃣ Exit")

        choice = input("\nEnter your choice: ")

        menu = {
            "1": register_user,
            "2": display_users,
            "3": find_user,
            "4": delete_user,
            "5": exit
        }

        action = menu.get(choice)
        if action:
            action()
        else:
            print("\n❌ Invalid choice. Please select a valid option.\n")

# Run the program
if __name__ == "__main__":
    main()
11