# rectangle.py

class Rectangle:
    def __init__(self, height, width):
        """
        Constructor to initialize the rectangle with height and width.
        """
        self.height = height
        self.width = width

    def area_of_rectangle(self):
        """
        Method to calculate the area of the rectangle.
        Formula: Area = height * width
        """
        return self.height * self.width

    def perimeter_of_rectangle(self):
        """
        Method to calculate the perimeter of the rectangle.
        Formula: Perimeter = 2 * (height + width)
        """
        return 2 * (self.height + self.width)


# Creating an instance of the Rectangle class
rectangle = Rectangle(2, 3)

# Calculating and printing the perimeter
print("Perimeter of the rectangle:", rectangle.perimeter_of_rectangle())

# (Optional) Calculating and printing the area
print("Area of the rectangle:", rectangle.area_of_rectangle())
