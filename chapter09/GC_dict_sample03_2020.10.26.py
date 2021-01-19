# Write a program that prints all key/value pairs on a separate line. The output should look like "Key: <KeyName>, Value: <Value>"
my_dict = {1: 'index number', 'first_name': 'Garett', 'last_name': 'Chang', 'favorite_numbers': [3, 5, 6, 6]}


for key, val in my_dict.items():
    print(f"Key: {key}, Value: {val}")