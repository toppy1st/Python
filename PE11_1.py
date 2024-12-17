#PE11_1

# a)    Class Declaration
class Rectangle:

# b)    Implementing an __int__ Method with Optional Parameter and Default Values
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

# c)    Creating a Display Method
    def display(self):
        print(f"\nWidth: {self.width}\nHeight: {self.height}")

# d)    Instantiating Objects of the Rectangle Class
r1 = Rectangle(4, 5)  
r2 = Rectangle()      

# e)    Calling the Display Method to Show Object Details
r1.display()
r2.display()

# f)    Displaying the 'width' and 'height' Attributes of 'r1' and 'r2'
print(f"\nWidth of r1 and r2:\n{r1.width} & {r2.width}")
print(f"\nHeight of r1 and r2:\n{r1.height} & {r2.height}\n")

