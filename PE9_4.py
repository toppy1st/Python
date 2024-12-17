#   PE9_4

#   Importing hello() function to PE9_4 file
from PE9_3 import hello

#   a)  Defining the helloNo() Function to Repeat hello() Based on User Input
def helloNo(n):
    for _ in range(n):
        hello()
        
n = int (input ("\nHow many times do you wanna print 'Hello World'?\n"))

#   b)  Using a Parameter to Control the Number of Loop Iterations in helloNo()
print (f"\nHelloNo({n}) will print the following:\n")
helloNo(n)  
print()