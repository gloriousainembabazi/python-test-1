# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

#answers
mark =int(input("Enter the mark score: "))
if mark>=90:
    print("Grade A")
elif mark>=80 and mark<=80:
    print("Grade B")
elif mark >=70 and mark<=70:
    print("Grade C")
elif mark >=60 and mark<=60:
    print("Grade D")
elif mark >=40 and mark <=40:
    print("Grade E")
else:
    mark < 40
    print("Grade F")




