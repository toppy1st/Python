# PE11_2

# i) & j)   Saving and Importing the Rectangle Class from rectangle.py
from rectangle import Rectangle  


# k)
# 1)    Instantiate two objects of type Rectangle
r1 = Rectangle(4, 5)
r2 = Rectangle()


# 2)    Call display() to print width and height
r1.display()
print(f"Area: {r1.area()}")  

r2.display()
print(f"Area: {r2.area()}")  


# 4)    Call setWidth() and setHeight() to update width and height to 6 for r2
r2.setWidth(6)
r2.setHeight(6)


# 5)    Call getWidth() in print() to display the updated width of r2
print(f"\nGet Width: {r2.getWidth()}")

# 6)    Call getHeight() in print() to display the updated height of r2
print(f"Get Height: {r2.getHeight()}")

# 7)    Call area() in print() to display the updated area of r2
print(f"Area: {r2.area()}\n")

# Running the whole code for the question in the same file can excute the ouput twice