#   PE10_5

print()

#   a)  Defining createUser() function with arbitrary dictionary parameter
def createUser(**kwargs):
    return kwargs

#   b)  Defining printUser() function with parameter user (a dictionary)
def printUser(user):
    for key, value in user.items():
        print(f"{key}: {value}")
        
#   c)  Creating and printing the user "John"
john = createUser(name = "John", age = 43, job = "Programmer", hobby = "Biking")
printUser(john)

print()

#   d)  Creating and printing the user "Sara" 
sara = createUser(name = "Sara", age = 20, school = "QCC", major = "CSIS")
printUser(sara)

print()
