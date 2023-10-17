#CREATE A VARIABLE
name = "James"
anotherName = "Nyamburi" #camelCaseMethod for naming variables
multiStr = """
JAMES
OTIENO
NYAMBURI
"""

x = 1
y = 1.5
z = True

#MAKE THE VARIABLE NAME UNDERSTANDABLE
firstName = "James"
secondName = "Nyamburi"

#VARABLES ARE CASE SENSITIVE
name = "James"
Name = "Nyamburi"

#A VARIABLE CAN CONTAIN VARIABLES
x = 1
y = x + 1 # 2

#OPERATIONS FOR VARIABLES
x = 2
y = 3
z = x * y # 6

#ASSIGN MULTILE VALUES 
player1, player2, player3 = "Ronaldo", "Messi", "Kaka"

#ASSIGN ONE VAUE TO MANY VARIABLE
striker1 = striker2 = striker3 = "Good players"
print(striker1, striker2, striker3)

#PRINTING VARIABLES
fruit1 = "banana"
fruit2 = "apple"
print("The fruit is "+ fruit1)
print("The fruit is", fruit2)

#CONVERT INTEGER TO STRING USING str IN BUILT FUNCTION TO ALLOW STRING CONCATINATION
x = 1
print("The value of x is "+ str(x))

#GET TYPE OF A DATA USING type BUILT IN FUNCTION
x = 1
y = 5.2
fruit = "MANGO"
numbers = [1, 2, 3]

print(type(x))
print(type(y))
print(type(fruit))
print(type(numbers))

print(type(0xFF))
