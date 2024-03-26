# string concat
str1 = "sherine"
str2 = 'Antony'

str3 = str1 + str2
print(str3)

age = 35
# str_age_name =  str1 + age
# print(str_age_name)     # TypeError: can only concatenate str (not "int") to str
str_age_name = str1 + str(age)
print(str_age_name)