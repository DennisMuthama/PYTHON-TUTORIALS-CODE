
# a zip function in python
#it used to assign values if i add gender and its only 
#print the values that meet all the qualification
names = ["dennis", "key glock", "teezy", "muthama"]
age = [20,34,54,65]

assigned_values = list(zip(names,age))

for name,age in assigned_values:
    print(f"my name is {name}, and my age is {age}")