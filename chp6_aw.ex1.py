#1. Write a program that opens an output file with the filename
#my_name.txt, writes your name to the file, then closes the file.

def outputfile(name):
    fileobject = open('c:\data\my_name.txt', 'a')
    fileobject.write(name)
    fileobject.write("\n")
    fileobject.close()

username = input(f"Please enter your first and last name:  ")

outputfile((username))