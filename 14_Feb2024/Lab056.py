# Functions
# Block of code - Which can executed
# They can return something
# They can't return  --> non return

# They have parameter or arguments
# function  --> Define & call

def say_hello():               # non Return type & No Parameter or argument
    print("Hello")
say_hello()


def say_hello_arg(name):    # non return type with parameter or argument
    print("Hello", name)
say_hello_arg("Sherine")

def say_hello_mult_arg(name,age):  # non return type with parameter or argument
    print("Hello", name, age)
say_hello_mult_arg("Sherine","67")
say_hello_mult_arg(123,True)

def say_hello_arg_default(name ="sherine 1"):    # non return type with default parameter
    print("Hello",name)
say_hello_arg_default( )
say_hello_arg_default(name= "Ginson 2")
say_hello_arg_default("Preethi 3")   # if passed value in function will display that value ie Preethi, otherwise will
# display default value sherine in function

def sum_number_arg(a,b):  # return argument
    return a + b

result = sum_number_arg(3,4)
result1 = sum_number_arg("Sherine"," Preethi")
result2 = sum_number_arg(a =10, b=90)
result3 = sum_number_arg("sherine", 26)  # TypeError: can only concatenate str (not "int") to str  , concatination not allowed
print(result)
print(result1)
print(result2)
print(result3)