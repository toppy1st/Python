#   PE9_5
import random

#   a)  message(p1, p2) - Looping to Print the Text
def message (p1,p2):
    for _ in range (p2):
        print (p1)
        
#   b)  Defining the main() Function
def main():
    
#   1)  Requesting input text from the console and printing it
    text = input ("\nEnter a text: ")
    print (f"text = {text.capitalize()}")

#   2)  Getting a random integer between 1 and 10
    n = random.randint(1, 10)
    print (f"n = {n}")

#   3)  Calling the message() function to display the text 'n' times
    print ("message (text, n) will print the following:\n")
    message(text.capitalize(),n)

# 4)    Input, Output, Processing, and Calling functions, everything handled

#   c)  Calling the main() Function
if __name__ == "__main__":
    main()
    
print()   