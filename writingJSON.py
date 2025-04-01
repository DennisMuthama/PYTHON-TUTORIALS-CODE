import json

def read_json(filename="account.json"):
    """Read the JSON file and return data."""
    try:
        with open(filename, "r") as file:
            return json.load(file)  # Convert JSON to Python object
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if file doesn't exist or is empty

def write_json(data, filename="account.json"):
    """Write data to JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def get_user_details():
    """Prompt user for input and store in JSON file."""
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    balance = input("Enter your balance: ")

    user_data = {
        "full_name": full_name,
        "phone_number": phone_number,
        "balance": balance
    }

    # Read existing data
    users = read_json()

    # Append new user data
    users.append(user_data)

    # Save updated data
    write_json(users)

    print("User details saved successfully!")

# Call function to get user input
get_user_details()
