from math import sqrt
x1 , y1 = 0 , 0
x2 , y2 = 3 , 4

#distance between two points
dist=sqrt(pow(x2-x1,2)+pow(y2-y1,2))  # method 2 >  dist = sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"distance={dist}")

'''
Assignment:
- Input from user (radius of a circle)
- print area (pi r^2)
- print circumference (2*pi*r)
- print diameter (2r)
'''
from math import pi
radius= float(input("Enter radius : "))
print(f"Area = {pi*(radius**2)}")
print(f"Circumference = {2*pi*radius}")
print(f"Diameter = {2*radius}")