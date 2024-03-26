# Problem to find the MAx between 3 numbers

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))

# max_number = max(num1,num2,num3)
# print("maxium number",max_number)

if num1 > num2 and num1 > num3:
    print("Max is", num1)
elif num2 > num1 and num2 > num3:
    print("Max is", num2)
else:
    print("Msx is", num3)
