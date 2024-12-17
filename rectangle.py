# rectangle

# a)    Class Declaration
class Rectangle:

# b)    Implementing an __init__ Method with Optional Parameter and Default Values
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
        
# c)    Creating a Display Method
    def display(self):
        print(f"\nWidth: {self.width}")
        print(f"Height: {self.height}")
        
# d)    Creating a setWidth Method to Assign Width to the Instance Variable
    def setWidth(self, width):
        self.width = width
        
# e)    Creating a setHeight Method to Assign Height to the Instance Variable
    def setHeight(self, height):
        self.height = height
        
# f)    Creating a getWidth Method to Access the Width Attribute
    def getWidth(self):
        return self.width
    
# g)    Creating a getHeight Method to Access the Height Attribute
    def getHeight(self):
        return self.height
    
# h)   Creating an area Method to Compute the Area of the Rectangle
    def area(self):
        return self.width * self.height