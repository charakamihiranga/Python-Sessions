# x = int(input("Input an number : ")) # normally user input is String

# if x % 2 == 0 :
#     print(x, "is even number")
# else :
#     print(x, "is odd number")    

# if x < 0 :
#     print(x, "is negative number")y:

# else :
#     if x%7 == 0 :
#         print(x, " is multiplication of 7")
#     else :
#         print(x, " is not a multiplication of 7")

# x = 3
# y = 4

# if x == y:
#     print("numbers are equal")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is less than y")

marks = int(input("Input marks : "))
if marks < 0 or marks > 100:
    print("Input Marks not allowed")
elif marks >= 85:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 65:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("F")