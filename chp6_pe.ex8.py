#chapter 6 Programming exercise exercise 8. Random Number File Reader This exercise assumes you have completed Programming
#Exercise 7, Random Number File Writer. Write another program that reads the random numbers from the file, displays the
#numbers, then displays the following data: The total of the numbers The number of random numbers read from the file

def summarytotal():
    total = 0

    filebojectread = open(r'c:\data\testrandom.txt', 'r')
    counter = 0
    for row in filebojectread:
        number = int(row.split(",")[1])
        total = total + number
        counter = counter + 1
    print(f"{counter}")
    print(f"{total}")



summarytotal()