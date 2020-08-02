#Algorithm Workbench exercise 3. Write code that does the following: opens an output file with the
#filename number_list.txt, uses a loop to write the numbers 1 through 100 to the file, then closes the file.

def openoutputfile():
    fileobject = open(r"c:\data\number_list.txt", 'w')

    for file in range(1,100 +1 ):
      name =f"{file} \n"
      fileobject.write(name)

    fileobject.close()

openoutputfile()

