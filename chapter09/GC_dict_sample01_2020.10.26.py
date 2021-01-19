
# Write a program that loops through the dictionary and prints all keys on a separate line
my_dict = {1:'index number', 'first_name': 'Garett', 'last_name': 'Chang', 'favorite_numbers': [3, 5, 6, 6]}

#for item in my_dict:
#    print(item)
my_keys = my_dict.keys()
for key in my_keys:
    print(f"Keys are:  {key}")

