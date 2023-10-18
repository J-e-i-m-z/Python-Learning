#declaring variable globally

x = 10 
def number():
    x = 16
    print(x) # Prints 16 because it is within the sope. x = 10 is declared globally 
number()

def number2():
    global x
    x = 10
    print(x)
number2()