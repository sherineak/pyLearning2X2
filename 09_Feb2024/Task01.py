# Interview Question task
# Create a program that determines whether a given year is leap year or not
# A leap year is divisible by 4 , but not by 100, It is also divisible by 400 and 100

year = int(input("Enter a year to find leap year"))

if year % 4 == 0 and year % 100 != 0:
    print(f"The year {year} is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print(f"The year{year} is a leap year")
else:
    print(f" the year is not a leap year")
