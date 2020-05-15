'''
workbench: exercise 4.
the following code contains several nested if-else statements.
Unfortunately, it was written without proper alignment and indentation.
Rewrite the code and user the proper convertions of alignment and indentation.
'''
score =  int(input(f"Please enter your grade: "))
A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 0
if score >= A_score:
    print(f" Your grade is A , you are a 'rock star' :")
elif score >= B_score:
    print(f"Your grade is  B")
elif score >= C_score:
    print(f"Your grade is C")
elif score >= D_score:
    print(f"Your grade is  D")
else:
    print(f"Your grade is F you have faile this semester, please retry ")