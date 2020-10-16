
telephone_characters =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
telephone_numbers =  "22233344455566677778889999"
tele_numbers = input("Please enter a phone number:  ").upper()

converted_numbers = ""
for phonenumber in tele_numbers:
    if phonenumber.isalpha():
        found = telephone_characters.find(phonenumber)
        letter = telephone_numbers[found]
        converted_numbers += letter
    else:
        converted_numbers += phonenumber


print(converted_numbers)

