class rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width


    def area_of_rectangle(self):
        return self.height * self.width
    
    def perimeter_of_rectangle(self):
        return 2 * (self.height + self.width)
    
perimeter = rectangle(2,3)

print(perimeter.perimeter_of_rectangle())