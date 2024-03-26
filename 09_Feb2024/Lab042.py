# # Write a program to calculate and display letter grade for a given numerical score
# (eg A, B, C, D, E and F) based on the score
# A: 90 - 100
# b : 80 - 89
# c: 70 - 79
# D : 60 - 69
# E : 50 - 59
# F : 0- 49
# else invalid

score = int(input("Please enter your Score \n"))

if score <= 100 and score >= 90 :
    print("Grade A")
elif score <= 89 and score >= 80:
    print("Grade B")
elif score <= 79 and score >= 70:
    print("Grade c")
elif score >=60 and score <=69:
    print("Grade D")
elif score >=50 and score <= 59:
    print("Grade E")
elif score >= 0 and score <= 49:
    print("Grade F")
else:
    print("invalid")