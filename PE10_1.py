#   PE10_1

print()

#   a)  Defining printList() function with one parameter p 
def printList(p):
    for item in p:
        print (item, end=" ")
    print ()
    
#   b)  Defining main() function
def main():

#   1)  Creating a list called lst[]
    lst = ['apple', 'banana', 'cherry']

#   2)  Calling printList() function with the lst argument
    printList(lst)
    
#   c)  Calling main() function
if __name__ == '__main__':
    main()
    
print()
    