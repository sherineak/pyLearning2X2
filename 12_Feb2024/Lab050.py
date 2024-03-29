# match case ==> Similar to switch

numbers = int(input("Enter the number"))
# BREAK NOT REQUIRED in case of  MATCH AND CASE , break will happen automatically

match numbers:
    case 1:
        print("The number is 1")
    case 2:
        print("The number is 2")
    case 3:
        print("The number is 3")
    case _:
        print("No idea")
