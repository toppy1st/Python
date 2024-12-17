#   PE10_6

import random

#   Computational Functions

print()

#   a)  Defining average() function to compute the average of an arbitrary number of grades
def average(*grades):
    if len(grades) == 0:
        return 0
    else:
        return sum(grades)/ len(grades)
    
#   b)  Defining main() function to execute the steps
def main():
    
#   1)  Calling average() function with provided arguments
    avg1 = average(95, 87, 83, 74)
    
#   2)  Creating two random integers
    x = random.randint(-100,0)
    y = random.randint(0,100)

#   3)  Calling average() function with random numbers
    avg2 = average(x, y)

#   4)  Printing all the results with the average computed to two decimal places
    print(f"Average of 95,87,83,74: {avg1:.2f}")
    print(f"Average of any two random numbers, {x}, {y}: {avg2:.2f}")

#   c)  Calling the main() function
if __name__ == "__main__":
    main()

print()
