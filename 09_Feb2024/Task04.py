#Fibonacci series  ==> Its important in Interview
#a = 10
#b = 12
# a, b = a, a + b
# print(a, b)
#  0, 1, 1, 2, 3, 5, 8, 13, 21  ( The some of the last two numbers )

a, b = 0, 1
while a < 10:
    print(a, end =" ")   # end = "" or end = "|"keep the numbers in the same line
    a, b = b, a + b
