print("Simple Calculator")
def addition(a,b):
    print("Addition of",a,"and",b,"is:",a+b)
def subtraction(a,b):
    print("Subtraction of",a,"and",b,"is:",a-b)
def multiply(a,b):
    print("Multiplication of",a,"and",b,"is:",a/b)
def divide(a,b):
    print("Division of",a,"and",b,"is:",a/b)
def power(a,b):
    print("Power of",a,"raised to",b,"is:",a**b)
choice = int(input("enter:\n1 for addition,\n2 for subtraction,\n3 for multiplication,\n4 for division,\n5 for finding power:\n"))
a=int(input("Enter num 1: "))
b=int(input("Enter num 2: "))
if choice == 1:
    addition(a,b)
elif choice == 2:
    subtraction(a,b)
elif choice == 3:
    multiply(a,b)
elif choice == 4:
    divide(a,b)
elif choice == 5:
    power(a,b)
