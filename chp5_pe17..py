""" Programming Exercise 17: A prime number is a number that is only evenly divisible by itself and 1.
For example, the number 5 is primebecause it can only be evenly divided by 1 and 5. The number 6, however, is not prime
because it can be divided evenly by 1, 2, 3, and 6. Write a Boolean function named is_prime which takes an integer as
an argument and returns true if the argument is a prime number, or false otherwise. Use the function in a program that
prompts the user to enter a number then displays a message indicating whether the number is prime. Tip: Recall that
the * operator divides one number by another and returns the remainder of the division. In an expression such as num1 %
 num2, the % operator will return 0 if num1 is evenly divisible by ."""
def is_prime(number):
    status = number % 2 == 0  or number % 3 == 0

    return not(status)


getnumber = int(input(f"Please enter a number: "))

result = is_prime(getnumber)

print(f"This is a prime number : {result}")
