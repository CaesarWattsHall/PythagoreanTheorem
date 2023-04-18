import math

side = input("Give the side you want to solve for (a, b, or c): ")

if side == "a":
    b = float(input("Give side b: "))
    c = float(input("Give hypotenuse c: "))
    a = math.sqrt(c ** 2 - b ** 2)
    print(f"The length of the side a is {a}")
    
elif side == "b":
    a = float(input("Give side a: "))
    c = float(input("Give hypotenuse c: "))
    b = math.sqrt(c ** 2 - a ** 2)
    print(f"The length of the side b is {b}")

elif side == "c":
    a = float(input("Give side a: "))
    b = float(input("Give side b: "))
    c = math.sqrt(a ** 2 + b ** 2)
    print(f"The length of the hypotenuse c is {c}")
else:
    print("Invalid input")
