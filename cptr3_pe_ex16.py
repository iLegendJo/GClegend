""" PE - exercise 16
February Days The month of February normally has 28 days. But if it is a leap
year, February has 29 days. Write a program that asks the user toenter a year. The program should then display the number of days
in February that year. Use the following criteria to identify leap years:
1. Determine whether the year is divisible by 100. If it is, then it is a leap year if and only if it is also divisible by 400. For
example, 2000 is a leap year, but 2100 is not. 2. If the year is not divisible by 100, then it is a leap year if and
only if it is divisible by 4. For example, 2008 is a leap year,but 2009 is not.
"""
year = int(input(f"enter a year: "))
month = "February"

leap_year = year%4
print(f"LeapYear: {leap_year}")
if  leap_year ==0:
    print(f"In {year} {month}  has 29 days " )
else:
    print(f"{year} is not a leap year")
