# Exercise 10. Feet to Inches - One foot equals 12 inches. Write a function named that accepts a number of feet
# as an argument and returns the number of inches in that many feet. Use the function in a program that prompts
# the user to enter a number of feet then displays the number of inches in that many feet.
def feet_to_inches(numberoffeet):
    foot = 12
    feet = numberoffeet * foot
    return feet

feet = int(input(f"Pleae enter a number of feet:"))
inches = feet_to_inches(feet)

print(f"This is the number of inches in many foot: {inches}")
