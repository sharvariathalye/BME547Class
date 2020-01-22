# calculator.py 

a = input("Enter the first number: ")
x = int(a) 
b = input("Enter the second number: ")
y = int(b)

def add(a, b):
    c = a + b
    return c, "+"
    
def subtract(a, b):
    c = a - b
    return c, "-"

def multiply(a,b):
    c = a * b
    return c , "x"

def divide(a,b):
    c = a / b
    return c , "/"

if __name__ == "__main__":
    a = x
    b = y
    answer, symbol = add(a, b)
    print("{} {} {} = {}".format(a, symbol, b, answer))
    answer, symbol = subtract(a, b)
    print("{} {} {} = {}".format(a, symbol, b, answer))
    answer, symbol = multiply(a,b)
    print("{} {} {} = {}".format(a, symbol, b, answer))
    answer, symbol = divide(a,b)
    print("{} {} {} = {}".format(a, symbol, b, answer))

    

