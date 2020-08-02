#Chapter 6 programming exercises exercise 3. Line Numbers Write a program that asks the user for the name of a file.
# The program should display the contents of the file with each line preceded with a line number followed by a colon.
# The line numbering should start at 1.

def nameoffile(filename):
    fileobject = open("c:/data/filename.txt", 'r')