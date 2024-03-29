# find factorial and fibonacci series
# fibonacci series -    The Fibonacci series is a sequence of numbers where each number is
# the sum of the two preceding ones 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# factorial   5!=5×4×3×2×1=120                        ,             4!=4×3×2×1=24

number = int(input("Enter the number to find factorial"))

if number < 0:
    print("The factorial is undefined")
elif number == 0:
    print("The factorial is 1 ")
else:
    fact = 1
    for i in range(1, number + 1):    # 1 to 5
        fact = fact * i
    print("factorial is ", fact)
