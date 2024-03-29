# define a function

def greet():
    print("Helo, how are you?")
greet()
print("***********")

# use function  in for loop
for i in range(5):
    greet()

print("*********")
# if  call this function, doesn't return , so how to make return function in Lab054
result = greet()
print(greet())