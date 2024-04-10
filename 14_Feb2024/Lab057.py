# *args  and **kargs

def f1(a =1 ,b= 1,c= 1):   # if give default value to argument ,
    # then can call one value in the function , otherwise wil be error
    return  a+b+c
f1()
f1(1)
f1(1,2,3)
result = f1(a=10,b=20,c=30)
print(result)


# * args ==> any number of argument

# def sum(a,b,c,d,e):
#     return a + b+ c+ d+ e
# r = sum(1,2,3,4,5)
# print(r)

def print_argument(* args):
    for i in args:
        print(i, end="")

print_argument(1)
print_argument(1,2)
print_argument(1,2,3)
print_argument(1,2,3,4)