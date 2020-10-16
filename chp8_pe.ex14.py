#This program reads numbers from a file into a list
#Open a file for reading.
fileobject = open("pbnumbers.txt", "r")
#strip and split the line by space deleminiter
#List comprehension
data = [line.strip().split(" ") for line in fileobject]
# close the file
fileobject.close()
#print(data)
box = [0]*69
print(f"this is box data:  {box}")
for numbers in data:
    for n in numbers:
        new_n = int(n)
        box[new_n-1] = box[new_n - 1] + 1

"""print(f"this is the 1st for loop data:  {data} ")
print(f"this is the 2ndst for loop data:  {numbers} ")
print(f"this is the 2nd for loop data:  {n} ")"""
for n in range(1,9 +1):
    print(f"Box {n}: {box[n-1]}")

empty_list_two = [[i,numb] for i,  numb in enumerate(box)]
new_sorted_listA = sorted(empty_list_two, reverse=True)[0:10]
new_sorted_listD = sorted(empty_list_two, reverse=False)[0:10]
print(f"The top 10 most commom numbers by frequency : {new_sorted_listA}")
print(f"The top 10 least common numbers by frequency: {new_sorted_listD}")



