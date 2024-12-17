#   PE10_2

#   Data Management Functions
print()

#   a)  Defining nameFormat() function with parameters first, middle and last
def nameFormat(first, middle, last):
    
#   1)  Printing by using proper title format
    print (f"{first.capitalize()} {middle[0].upper()}. {last.title()} ")

#   b)  Defining main() function  
def main():
    
#   1)  Calling nameFormat() function with positional arguments
    nameFormat("john", "stu", "smith")

#   2)  Calling nameFormat() funcion with keywords arguments
    nameFormat(first = "john", middle = "fitzgerald", last = "kennedy")
    
#   c)  Calling main() function
if __name__ == "__main__":
    main()  
    
print()
  