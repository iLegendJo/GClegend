#Write code that does the following: opens the number_list.txt file #that was created by the code you wrote in
# question 3, reads all of #the numbers from the file and displays them, then closes the file.

def openreadfile():
    fileobject = open("/data/number_list.txt", 'r')

    for row in fileobject:
        print(f"This is the number:  {row}".strip())
    fileobject.close()

openreadfile()

