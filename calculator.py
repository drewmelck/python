print("Welcome to the calculator,you can use the following operators:+,-,/,*,%" )
x = input("Enter a number: ")
a = raw_input("Operator: ")
y = input("enter a second number: ")
if a == "+":
    print(x + y)
elif a == "/":
    print(x / y)
elif a == "-":
    print(x - y)
elif a == "*":
    print(x * y)
else:
    print("Invalid operator")
