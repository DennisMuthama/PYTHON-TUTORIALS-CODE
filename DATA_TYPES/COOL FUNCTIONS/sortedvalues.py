people_details = [
    {"name":"dennis", "age":23, "money":23000},
    {"name":"tate", "age":45, "money":2309900},
    {"name":"zues", "age":203, "money":200},
    {"name":"muthama", "age":73, "money":2800000},
]

sorted_info =sorted(people_details, key=lambda person: person["age"])
print(list(sorted_info))







#using the sorted values in python

# my_numbers = [2, 3,535,563,53]

# sorted_values = sorted(my_numbers,reverse=True)
# print(list(sorted_values)