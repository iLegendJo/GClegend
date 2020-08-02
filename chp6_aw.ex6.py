#chapter 6 algorithm workbench exercise 6. Write code that opens an output file with the filename number_list.txt,
# but does not erase the file’s contents if it already exists.

def openoutputfile():
    fileobject = open("c:/data/number_list.txt", 'a')

    fileobject.close()


openoutputfile()