#" exercise 7. The following statement calls a function named  half, which
#returns a value that is half that of the argument. (Assume the number
#variable references a float value.) Write code for the function. "

def half(number):
    total = 0.0
    total = number / 2

    return total

value = float(input(f"Please enter a number:"))
result = half(value)
print(f"This is the half of the argument: {value}  {result}")
