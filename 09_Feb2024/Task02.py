# Write a program that classifies a triangle bases on its length of sides
# the triangle are equilateral(all sides are equal) or isosceles (exactly two sides are equal)
# or scalene (no sides are equal)

side1 = float(input("Enter first side"))
side2 = float(input("Enter the second side"))
side3 = float(input("Enter the third side"))

if side1 == side2 and side2 == side3 and side1 == side3:   # Or can use side1 == side2 == side3
    print(" The traingle is equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The traingle is isosceles")
else:
    print("The  traingle is scalene ")