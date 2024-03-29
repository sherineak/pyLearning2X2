#  Break

for counter in range(1, 10):
    if counter == 5:
        break             # break or stop once reached counter ==5
    print(counter)
print("Outside of the for loop")


for i in range(0,11):
    print(i)
    if i == 5:
        break
print("Outside of the for loop")