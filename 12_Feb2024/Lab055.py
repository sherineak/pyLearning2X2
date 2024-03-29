def sum_of_num(a,b):
    return a+b

result = sum_of_num(4,5)
print(result)

result = sum_of_num(3.5, 4.5)
print(result)

result = sum_of_num("sherine", "Antony")
print(result)

# no need to specify data , this will take any data types but one string and integer in same function not allow, pls check with examples

result = sum_of_num("Sherine",23)   # TypeError: can only concatenate str (not "int") to str
print(result)