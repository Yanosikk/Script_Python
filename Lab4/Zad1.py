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
    
    
point_1 = Point(1.2, 2)
point_2 = Point(1.3, 3)
point_3 = Point(1.4, 4)
    
    
print("Coordinates point_1: ", point_1)
print("Distance of point_1 from the origin of the coordinate system:", point_1.distance())

print("\nCoordinates point_2:", point_2)
print("Distance of point_2 from the origin of the coordinate system:", point_2.distance())

print("\nCoordinates point_3:", point_3)
print("Distance of point point_3 from the origin of the coordinate system:", point_3.distance())

print("\nDistance between point_1 and point_2:", point_1.distance_between(point_2))
print("Distance between point_1 and point_3:", point_1.distance_between(point_3))