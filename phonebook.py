import json
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = Contact(name, phone, email)
    print(f"Contact {name} added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
    else:
        for contact in contacts.values():
            print(contact)

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name].phone = phone
        contacts[name].email = email
        print(f"Contact {name} updated.")
    else:
        print(f"Contact {name} not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

def save_contacts_to_file(contacts, filename):
    with open(filename, 'w') as file:
        json_contacts = {name: contact.__dict__ for name, contact in contacts.items()}
        json.dump(json_contacts, file)
    print("Contacts saved to file.")

def load_contacts_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            json_contacts = json.load(file)
            return {name: Contact(**data) for name, data in json_contacts.items()}
    return {}

def main():
    filename = 'contacts.json'
    contacts = load_contacts_from_file(filename)
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts_to_file(contacts, filename)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
