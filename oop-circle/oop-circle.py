class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
       return (22/7)*(self.radius)**2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius


c1 = circle(int(input("Enter the radius of circle: ")))
print("Area of the circle is ",c1.area())
print("Perimeter of the circle is ",c1.perimeter())