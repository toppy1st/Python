#   PE12_1

print()

#   Using Loop
def readWloop(UsPres):
    print("Using Loop -----")  
    with open(UsPres, 'r') as file:
        for i, line in enumerate (file):
            if i < 3:
                print (line.strip())
            else:
                break


#   Using List
def readWlist(UsPres):
    print("Using List -----")
    with open(UsPres, 'r') as file:
        lines = file.readlines()  
        for line in lines[:3]:
            print(line.strip())  

#   Building and calling main function
def main():
    UsPres = "/Users/thirihtet/Desktop/QBCC/Python/FilesExceptionsExamples/USPres.txt"
    readWloop(UsPres)
    print()
    readWlist(UsPres)

if __name__ == "__main__":
    main()
    
print()

