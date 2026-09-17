import math
def add(a,b):
    print("Sum:" a+b)

def subtract(a,b):
    print("Subtraction:", a-b)

def multiply(a,b):
    print("Multiplication:", a*b)

def divide(a,b):
    print("Division:", a/b)

print("-----Calculator Menu-------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice(1-5):"))

if choice == 1:
    a = int(input("Enter num1:"))
    b = int(input("Enter num2:"))
    print("Sum of", a, "and", b, "is:", add(a,b))

elif choice == 2:
    a = int(input("Enter num1:"))
    b = int(input("Enter num2:"))
    print("Subtraction of", a, "and", b, "is:", subtract(a,b))

elif choice == 3:
    a = int(input("Enter num1:"))
    b = int(input("Enter num2:"))
    print("Multiplication of", a, "and", b, "is:", multiply(a,b))

elif choice == 4:
    a = int(input("Enter num1:"))
    b = int(input("Enter num2:"))
    print("Division of", a, "and", b, "is:", divide(a,b))

elif choice == 5:
    print("Exiting..")
else:
    print("Invalid Choice")

