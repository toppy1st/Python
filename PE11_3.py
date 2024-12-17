# PE11_3.py

# i) & j)
from shapes import Rectangle,Circle        


#   Instantiating Objects of the Rectangle Class
r1 = Rectangle(1, 1)   
r2 = Rectangle() 

#   Display the details of Rectangle r2 before changes
r2.display()


#   Update the width and height of r2 and display updated information
r2.setWidth(1.25)
r2.setHeight(1.25)
print(f"Get Width: {r2.getWidth()}")
print(f"Get Height: {r2.getHeight()}")
print(f"Area: {r2.area():.5f}")

#   Instantiating Objects of the Circle Class
c1 = Circle()
c2 = Circle(10)

print(f"\nRadius: {c1.getRadius()}")  # The output will be 1 as we set the default value as 1
print(f"Get Radius: {c2.getRadius()}")
print(f"Area: {c2.area():.5f}")
print(f"Circumference: {c2.circumference():.5f}\n")
