# shapes

# a)
from math import pi

# Rectangle Class (the same code as the previous question)
class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
        
    def display(self):
        print(f"\nWidth: {self.width}")
        print(f"Height: {self.height}")
        
    def setWidth(self, width):
        self.width = width
        
    def setHeight(self, height):
        self.height = height
        
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def area(self):
        return self.width * self.height
    
# b)    Class Declaration
class Circle:

# c)    Implementing an __init__ Method with Optional Parameter and Default Value
    def __init__(self, radius = 1):
        self.radius = radius
        
# d)    Creating a Display Method
    def display(self):
        print (f"\nRadius: {self.radius}")

# e)    Creating a setRadius Method to Assign Radius to the Instance Variable     
    def setRadius(self, radius):
        self.radius = radius

# f)    Creating a getRadius Method to Access the Radius Attribute
    def getRadius(self):
        return self.radius

# g)   Creating an area Method to Compute the Area of the Circle
    def area(self):
        return pi * (self.radius ** 2)
    
# h)   Creating a circumference Method to Compute the Circumference of the Circle
    def circumference(self):
        return 2 * pi * self.radius