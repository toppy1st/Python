#   PE9_1

import math 

#   a)  Building input function for two numbers with Validation to ensure denominator is not '0'
while True:

    numerator = int(input("\nEnter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    if denominator != 0:
        break
    print ("Denominator cannot be zero. Try again.\n")

#   b)  Using math.fmod() function to calculate the remainder of the user input
remainder = math.fmod(numerator, denominator)

#   c)  Printing the remainder as an integer
print (f"{numerator} mod {denominator} = {int(remainder)}\n")
