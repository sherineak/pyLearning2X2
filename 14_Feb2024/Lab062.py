# lambda Expression  ==> rarely seed, moslty used in data science
# to help you guys
# f(n) --> one liner python

# def double_my_salary(salary):
#     return salary * 2
# result = double_my_salary(1000)
# print(result)


d_salary = lambda salary: salary * 2
print(d_salary(10))

pow_of_two = lambda num: num **2
print(pow_of_two(10))

sum = lambda a,b,c: a+b+c
print(sum(3,4,5))

say_my_name = lambda name: print(" your name",name)
say_my_name("Sherine")