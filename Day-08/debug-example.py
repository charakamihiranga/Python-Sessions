import pdb

def multiplication(a, b):
    answer = a * b
    return answer


pdb.set_trace()

x = input("Enter first number: ")
y = input("Enter second number: ")

mul = multiplication(x, y)
print(mul)