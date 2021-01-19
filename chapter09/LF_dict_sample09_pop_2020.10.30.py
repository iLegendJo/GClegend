phonebook = {'Chris': '555-1111',
             'Katie': '555-22222',
             'Joanne':' 555-33333'}
phone_num = phonebook.pop('Chris', 'Entry not found')
print(phone_num)
print(phonebook)
phone_num = phonebook.pop('Andy', 'Element not found')
print(phone_num)
print(phonebook)
