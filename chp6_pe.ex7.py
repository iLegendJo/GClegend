import random

def randomnumbers(counter):
    fileboject = open(r'c:\data\testrandom.txt', 'w')

    for number in range(1, counter + 1):
        randomnumbers = (random.randrange(1, 500, 1))
        line = (f"{number},{randomnumbers}\n")
        fileboject.write(line)
        print(line)


userrandomnum = int(input(f"How many randoms numbers do you want the file to hold:  "))


randomnumbers(userrandomnum)