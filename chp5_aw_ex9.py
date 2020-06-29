#Write a function named times_ten that accepts a number as an argument. When the function is called,
# it should return the value of its argument multiplied times 10.

def times_ten(number):
    total = 10
    result = number * total
    return result

value = int(input(f"Please enter a number: "))
finalvalue = times_ten(value)
print(f"This is is the value of the number muktiplied by 10:  {finalvalue}")
