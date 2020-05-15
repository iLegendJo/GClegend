'''Programming Exercises •	Exercise 2
The area of a rectangle is the rectangle's length times its width.
Write a program that asks for the length and width of two rectangles.
The program should tell the user which rectangle has the greater area,
or if the areas are the same.
'''


length = float(input(f"Please enter a value for lenght: "))
width = float(input(f"Please enter a value for lenght: "))

area = length * width
print(f"The area is: {area}")

print('**********************************************************************************************')
length2 = float(input(f"Please enter a value for lenght: "))
width2 = float(input(f"Please enter a value for lenght: "))

area2 = length2 * width2
print(f"The area is: {area2}")

if area >= area2:
 print(f"rectangle1 {area} is greater than rectangular area 2 is {area2}")
else:
 print(f"rectangle area 2: {area2} is greater than rectangular area 1:  is {area}")