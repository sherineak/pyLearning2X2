# Write factorial using function
# default 1

def factorial(n):

    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range( 1, n + 1):  # OR (2, n + 1 )
            fact = fact * i
        return fact
num = 6
print(f"The factorial of {num} is",factorial(num))

# ******OR*********

def fac(n1):
    if n1 < 0:
        print("The number is undefined")
    elif n1 == 0 or n1 == 1:
        print("The factorial is 1")
    else:
        f1 = 1
        for i in range (1,n1+1):
            f1 = f1 * i
        print(f"The factorial of  {n1} is {f1}")

# Taking input from the user
number = int(input("Enter the number"))
# calling the function with the input number
fac(number)
