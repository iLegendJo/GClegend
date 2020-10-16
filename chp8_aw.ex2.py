temp = input(f"Please enter value: ")
counter= 0
for letter in temp:
    #print(letter)
    if letter.isspace():
       counter = counter + 1
print(f"this is the number of space(s): {counter}")