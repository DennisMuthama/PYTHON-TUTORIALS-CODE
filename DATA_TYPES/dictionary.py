#they take both strings and integers,written using curly brackets
#they need to be assigned  values with a colon

my_dictionary={"name":"dennis", "age": 20,"sister": "betty"}
print(my_dictionary["name"])

# Dictionary of products and their prices
# products = {
#     "apple": 0.99,
#     "banana": 0.50,
#     "cherry": 1.20,
#     "date": 1.50
# }

# # Using 'for item in items' to iterate over the dictionary items
# for product, price in products.items():
#     print(f"The price of {product} is ${price}")
    

#to access ecah key of the dictionary

#to update a dictionary
my_dictionary.update({"name":"muthama"})

for key,value in my_dictionary.items():
    print(f"the key is: {key} and the value is {value}")