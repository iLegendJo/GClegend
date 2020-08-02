#Chapter 6  - Algorithm Workbench exercise 5. Modify the code that you wrote in problem 4 so it adds all of the
#numbers read from the file and displays their total.

def openreadfile():
    fileobject = open("/data/number_list.txt", 'r')
    counter = 0
    for row in fileobject:
        total = (f" {row}".strip())
        counter = counter + int(total)
    print(f"The total read from problem 4 file is: {counter}")
    fileobject.close()

openreadfile()

