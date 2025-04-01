#an exercise
# def search_item(item, item_list):
#     try:
#         return item_list.index(item)
#     except ValueError:
#         return -1

# result = search_item("apple", ["banana", "cherry", "date"])
# if result == -1:
#     print("Item not found")


username=input("enter your name: ")

if len(username) > 12:
    print("your name cant be more than 12 characters")
elif  username.find("-") != -1:
        print("Your username cant contain dashes")
elif  username.find("k") != -1:
        print("letter K cant be printed")
else:
    print(f"welcome {username}")