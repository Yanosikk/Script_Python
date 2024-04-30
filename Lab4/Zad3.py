import math

class Point:
    def __init__(self, x = 0, y = 0): 
        self.x = x
        self.y = y 
        
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def distance_between(self, dif_point):
        return math.sqrt((self.x - dif_point.x)**2 + (self.y - dif_point.y)**2)

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __str__(self):
        return f'Point({self.x}, {self.y})'

class Circle(Point):
    def __init__(self, x=0, y=0, r=1):
        super().__init__(x, y)
        self.r = r

    def __repr__(self):
        return f'Kolo({self.x}, {self.y}, {self.r})'

    def __str__(self):
        return f'A circle with a center {Point.__repr__(self)} and radius {self.r}'
    
    def circuit(self):
        return 2 * math.pi * self.r

    def field(self):
        return math.pi * self.r**2
    
    
circle_1 = Circle(2, 3, 2)
print("Object's text:", circle_1)
print("Distance of circle's center from the origin of the coordinate system:", circle_1.distance())
print("Radius:", circle_1.r)
print("Obwód koła:", circle_1.circuit())
print("Pole koła:", circle_1.field())


