# Continue

for num in range(1,10):
    if num % 2 == 0:
        print(f"The number {num} is even number")
    else:
        print(f" The Number {num} is odd number ")


# The above same with "continue"

for num in range(1,10):
    if num % 2 == 0:
        print(f"The number {num} is even")
        continue
    print(f"The number {num}is odd")