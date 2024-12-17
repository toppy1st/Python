#   PE9_6

import random

# a)    Defining the middle() Function
def middle(l):

# 1)    &   2)
    if len(l) > 2:
        return l[1:-1]
    elif len(l) <= 2:
        return []


# b)    Defining the main() Function
def main():

# 1)    Creating a list, numList with n numbers in the list
    numList = [random.randint(1, 100) for _ in range(random.randint(1, 10))]
    if len(numList) < 2:
        print("\nNo change made to the list.")

# 2)    Print the original list and its length
    print(f"\nList length = {len(numList)}")
    print(numList)
    
# 3)    Call middle(numList) function and print the returned list
    result = middle(numList)
    print(result)
    
# 4)    Input, Output, Processing, and Calling functions, everything handled

# c)    Calling the main() Function to Execute the Program
if __name__ == "__main__":
    main()

print ()