#BUILT IN FUNCTIONS 

#Get the type
x = 1 
print(type(x))

#Get user input
"""
name = input("ENTER YOUR NAME: ")
print("YOUR NAME IS:", name)

"""

#Convert a to integer
x = 10.1
print(type(x))
print(int(x))

y = str(12.5)
print(type(y))

z = float(9)
print(z)

#USER DEFINED FUNCTIONS

#Defining a function
def multiplyFunc(x):
    result = x * x
    return result

#Calling the function
print(multiplyFunc(5))
print(multiplyFunc(4))
print(multiplyFunc(3))
print(multiplyFunc(2))

#Add many parameters and Pass many arguments

def multiplyFunc(x, y):
    result = x * y
    return result
print(multiplyFunc(5, 6))
print(multiplyFunc(10, 10))

#Return many values
def arithmeticFunc(x, y):
    sum = x + y
    multiply = x * y
    divide = x / y
    return sum, multiply, divide

print(arithmeticFunc(1, 2))

#ANONYMOUS FUNCTION (Function defined without any name)
num = lambda x, y, z: x + y + z
print(num(1, 2, 3))

#Returning lambda
def new(y):
    return lambda x: x * y

double = new(2)
triple = new(3)

print(double(5))
print(triple(5))

