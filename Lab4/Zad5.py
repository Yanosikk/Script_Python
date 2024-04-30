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
    
    def move(self, vector):
        self.x += vector[0]
        self.y += vector[1]

class Circle(Point):
    def __init__(self, x=0, y=0, r=1):
        super().__init__(x, y)
        self.r = r

    def __repr__(self):
        return f'Circle({self.x}, {self.y}, {self.r})'

    def __str__(self):
        return f'A circle with a center {Point.__repr__(self)} and radius {self.r}'
    
    def circuit(self):
        return 2 * math.pi * self.r

    def field(self):
        return math.pi * self.r**2
    
    def move(self, vector):
        super().move(vector)
        
    def common_part(self, different_circle):
        distance_between_centers = self.distance_between(different_circle)
        radius_sum = self.r + different_circle.r
        return distance_between_centers > radius_sum

circle_1 = Circle(0, 0, 3)
circle_2 = Circle(9, 0, 2)

circle_3 = Circle(0, 0, 6)
circle_4 = Circle(6, 0, 1)
print("Circles with common part", circle_1.common_part(circle_2))
print("Circles without common part", circle_3.common_part(circle_4))  