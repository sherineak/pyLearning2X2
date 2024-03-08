name = 'batman'
print(type(name))
print(len(name)) # len strats from 1  , but index starts from 0, index[0]  = b for name batman
print(name[4])
print(name[5])
# print(name[6])  # IndexError: string index out of range
print(len(name)-2)
print(name[len(name)-1])

#string immutability

string = "Hello"
string = "Sherine"
print(string)
# string[0] = "p"  # TypeError: 'str' object does not support item assignment


