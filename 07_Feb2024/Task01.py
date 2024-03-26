# write a program to calculate the area of circle given its radius using the formula πr2
# r = input("Enter the radius")   TypeError: can't multiply sequence by non-int of type 'float'


import math  # To import value of pie from library (to get prebuilt values)
r = float(input("Enter the radius"))

area = 3.14 * r * r
print(area)
area = math.pi * pow(r,2)   # use library to get value of pie and use pow(r,2)
print(area)
