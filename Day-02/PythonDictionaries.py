# Dictionaries are ordered, changeable, does not allowed duplicates..

# my_dict = {
#     "name" : "Sugar",
#     "price" : 250.20,
#     "weight" : "1kg" 
# }

# print(my_dict) # {'name': 'Sugar', 'price': 250.2, 'weight': '1kg'}
# print(type(my_dict)) #dict

my_dict = {
    "name" : "Sugar",
    "price" : 250.20,
    "weight" : "1kg",
    "name" : "Rice"
}

print(my_dict) # {'name': 'Rice', 'price': 250.2, 'weight': '1kg'}
print(type(my_dict)) #dict
print(my_dict["price"]) # 250.2
my_dict["price"] = 300
print(my_dict)

print(my_dict.get("price")) # 300
print(my_dict.get("expire-date")) # None
print(my_dict.get("expire-date", "2025.02.03")) # 2025.02.03

my_dict.update({"price" : 100, "weight" : "2kg"}) # we have to pass an dictionary
print(my_dict) # {'name': 'Rice', 'price': 100, 'weight': '2kg'}

# adding completely new value to dictionary
my_dict["color"] = "white"
print(my_dict)

# to remove an item
# my_dict.pop("weight")
print(my_dict) # {'name': 'Rice', 'price': 100, 'weight': '2kg', 'color': 'white'}
del my_dict["weight"]
print(my_dict) # {'name': 'Rice', 'price': 100, 'color': 'white'}

print("length of my_dict", len(my_dict))
# del my_dict
# print(len(my_dict))

my_dict.clear()
print(my_dict) # {}

my_dict1 = {
    "name" : "Sugar",
    "price" : 250.20,
    "weight" : "1kg",
    "name" : "Rice"
}

my_dict = my_dict1.copy()
print(my_dict1) # {'name': 'Rice', 'price': 250.2, 'weight': '1kg'}