print("Select operation.")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
a = input("Enter choice (1/2/3/4):")





x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

def add(x, y):
        return x + y

def devide(x, y):    
        return x / y
def subtract(x, y):     
        return x - y
    
def multiply(x, y):   
        return x * y
if a == '1':
    print(x,"+",y,"=", add(x, y))
elif a == '2':
    print(x,"-",y,"=", subtract(x, y))
elif a == '3':
    print(x,"*",y,"=", multiply(x, y))
elif a == '4':
    print(x,"/",y,"=", devide(x, y))
else:
    print("Invalid operator")

