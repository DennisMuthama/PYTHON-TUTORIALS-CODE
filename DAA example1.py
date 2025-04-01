# #builduing a simple user authetication purely using python
# name=input("enter your name:")
# age = int(input("enter your age:"))
# password=input("enetr your password:")
# passz="MUTHAMa"
    
# try:
#     if not name == "":
#         print("proceed to enter you age")
#     else:
#         print("re-enter your name:")
    
#     if age > 100 and age < 0:
#         print("invalid age bro")
#     else:
#         print("procced to input your password")
    
#     while password == passz:
#         print("welcome to the system buddy")
    
#     print("incorrect password...re-enter password!! ")
    


# except  ValueError as e:
#         print(e)
# Sample data to simulate a user database
user_database = {
    "user1": "password123",
    "user2": "mypassword",
}

def authenticate(username, password):
    """Check if the username and password match an entry in the database."""
    if username in user_database:
        stored_password = user_database[username]
        
        if password == stored_password:
            return "Authentication successful!"
        else:
            return "Invalid password. Try again."
    else:
        return "Username not found."

# Example of usage
username = input("Enter your username: ")
password = input("Enter your password: ")

print(authenticate(username, password))

        