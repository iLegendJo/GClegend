
def determine_grade(grade):
    lettergrade = 'f'
    if grade >= 90:
        lettergrade = "A"
    elif grade <= 89.9 and grade >=80:
        lettergrade = "B"
    elif grade <= 79 and grade >= 70:
        lettergrade = "C"
    elif grade <= 69.9 and grade >= 60:
       lettergrade = "D"
    elif grade <= 60:
       lettergrade = "F"
    return lettergrade

def calc_average(grades5):
    average_grade = (grades5)/5
    return average_grade

testscores = range(1, 5  + 1)
result = 0
for grade in testscores:
   inputgrade =  float(input(f"Please enter a grade {grade}:"))
   result = result + inputgrade

average = calc_average(result)
letter_grade = determine_grade(average)
print(f"Average grade result : {average} Letter Grade is: {letter_grade} ")






