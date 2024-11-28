
# import my_calculator.addition
# import my_calculator.subtraction

# print(my_calculator.addition.add(5, 3))
# print(my_calculator.subtraction.subtract(5, 3))


# #Import entire module
# from my_calculator import addition
# from my_calculator import subtraction

# print(addition.add(5, 3))
# print(subtraction.subtract(5, 3))

# #Import specific function
from my_calculator.addition import add
from my_calculator.subtraction import subtract

print(add(5, 3))
print(subtract(5, 3))