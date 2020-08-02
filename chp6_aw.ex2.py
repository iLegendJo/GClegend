# chapter 6 Algorithm Workbench exercise 2. Write a program that opens the file that was created
# by the program in problem 1, reads your name from the file, displays the name on the screen, then closes the file.

def openoutputfile():
    fileobject = open("c:\data\my_name.txt", 'r')
    name = fileobject.readline()
    print(f"My name is {name}")
    fileobject.close()


openoutputfile()
