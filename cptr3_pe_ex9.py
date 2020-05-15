''' •	PE - Exercise 9
Roulette Wheel Colors On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are as follows:
Pocket 0 is green
For pockets 1 through 10, the odd-numbered pockets are red
and the even-numbered pockets are black.
For pockets 11 through 18, the odd-numbered pockets are
black and the even-numbered pockets are red.
For pockets 19 through 28, the odd-numbered pockets are red
and the even-numbered pockets are black.
For pockets 29 through 36, the odd-numbered pockets are
black and the even-numbered pockets are red.
'''
msg = "is invalid and outside the range of 0 through 36, please enter number between 0 through 36 "
roulette = {  0:"Green",1:"Red",2:"Black",3:"Red",4:"Black",5:"Red",
              6:"Black",7:"Red",8:"Black",9:"Red",10:"Black",11:"Black",
             12:"Red",13:"Black",14:"Red",15:"Black",16:"Red",17:"Black",
             18:"Red",19:"Red",20:"Black",21:"Red", 22:"Black",23:"Red",
             24:"Black",25:"Red",26:"Black",27:"Red",28:"Black",29:"Black",
             30:"Red",31:"Black", 32:"Red",33:"Black",34:"Red",35:"Black",36:"Red"}

pocket = int(input(f"Please entera pocket number: "))
#roulette[pocket]
if pocket <= 36 and pocket >=0:
    print(f"Pocket {pocket} is  {roulette[pocket]}  ")
else:
    print(f"Pocket {pocket} is {msg}  ")