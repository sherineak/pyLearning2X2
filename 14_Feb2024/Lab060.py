# Reverse a string


def rev_string_input(strval):
    rev = ""
    for c in strval:
        rev = c + rev
    print("Reverse string",rev)

name1 = input("enter the name to reverse ")
rev_string_input(name1)
print("*****************")


def reverse_string(str):
    rev_str = "" # empty string
    for c in str:
        rev_str = c + rev_str
    return rev_str

orginal_str = input("Pls enter the string to check palindrone")
# orginal_str = orginal_str.lower()
rev_str = reverse_string(orginal_str)
if orginal_str == rev_str:
    print("Its palindrone")
else:
    print("Not palindrone")

name = reverse_string("Sherine")
print("Reverse String",name)


# Palindrone if String = reverse string
