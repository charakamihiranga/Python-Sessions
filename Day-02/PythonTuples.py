#Python Tuples - (Tuples are immutable, ordered and allow duplicates, tuple items are indexed)

# my_tuple = ("Apple", "Orange", "Grapes", "Banana")
# print(type(my_tuple)) #tuple
# print(len(my_tuple)) #4

# my_tuple = (8)
# print(type(my_tuple)) #int
# my_tuple1 = (8,)
# print(type(my_tuple1)) #tuple

# my_tuple = (8,4,7,5,6)
# print(my_tuple[-2]) #5 negative indexing are allowed

# my_tuple = (8,4,7,5,6)
# print(my_tuple[1:3]) # (4, 7)

#tuple values can be change in alternative way
# my_tuple = (8,4,7,5,6)
# my_list = list(my_tuple)
# print(my_list)
# print(type(my_list))
# my_list[2] = 100
# print(my_list) #list
# my_tuple = tuple(my_list)
# print(my_tuple)
# print(type(my_tuple)) # tuple

# #Nested Tuples
# my_tuple = ((1,3,2), ("Apple", "Grapes", "Banana", "Orange"), (True, False))
# print(my_tuple[1][2]) #Banana
# print(my_tuple[2][1]) #False