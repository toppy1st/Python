#   PE9_2

import random
import math

#   a)  Gererating a random number using randint() from the random module
rand_num = random.randint (1,100)

#   b)  Calculating the integer square root using isqrt()
sq_num = math.isqrt (rand_num)

#   c)  Printing the integer square root of the random number
print (f"\nSquare root of {rand_num} = {sq_num}\n")

