def times_ten(product):
    total = 0
    total = product * 10
    return total



number = int(input(f"please enter a value:"))
answer = times_ten(number)

print(f"this is total: {answer}")