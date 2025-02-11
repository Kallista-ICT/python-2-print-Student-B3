import math

a = float(input("How many ax2 :"))
b = float(input("How many bx :"))
c = float(input("How many c:"))

x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
x2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a

print(f"The answer is {x1} and {x2}")
