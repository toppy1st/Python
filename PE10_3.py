#   PE10_3

print()

#   a)  Defining nameFormat() function with parameter first, last and middle(Optional parameter)
def nameFormat(first, last, middle=""):
    if middle:
        return f"{last.capitalize()}, {first.capitalize()}, {middle[0].upper()}."
    else:
        return f"{last.capitalize()}, {first.capitalize()}"

#   b)  Defining main() function
def main():
    
#   1)  Calling the function with keyword arguments for the name
    Nomiddle = nameFormat(first="james", last="bond")
    
#   2)  Calling the function with keyword arguments for the name
    Withmiddle = nameFormat(first = "henry", middle="indiana", last="jones")
    
#   3)  Printing the results of the function calls

    print (Nomiddle)
    print (Withmiddle)
    
#   c)  Calling the main() function
if __name__ == "__main__":
    main()

print()
