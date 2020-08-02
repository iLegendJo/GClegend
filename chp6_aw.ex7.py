#chapter 6 Algorithm Workbench exercise 7 - A file exists on the disk named students.txt. The file contains
# several records, a # nd each record contains two fields: (1) the student’s name, and (2) the student’s
# score for the final exam. Write code that deletes the record containing “John Perz” as the student name.

def deletingrecords():
    fileobject = open("c:/data/students.txt", 'r')

    for file in fileobject:
        print(f"thiis the value: {file}")

deletingrecords()