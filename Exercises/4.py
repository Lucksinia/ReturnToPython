# 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
import math

radius = float(input("input radius with floating point: "))

area = math.pi * radius**2
print(f"The area of your sircle is: {area:.04}")
