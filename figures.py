import math


class Square():
    def __init__(self, side,):
        self.side = side

    def area(self):
        return (self.side**2)

    def perimeter(self):
        return (4*self.side)


class Circle():
    def __init__(self, r):
        self.radius = r

    def circumfrence(self):
        return 22/7*self.radius * 2

    def area(self):
        return 22/7 * (self.radius**2)


class Rhombus():
    def perimeter(self):
        l = float(input("Enter the 1st side"))
        b = float(input("Enter the 2nd side"))
        return 2*(l+b)

    def area(self):
        l = float(input("Enter the 1st daigonal"))
        b = float(input("Enter the 2nd daigonal"))
        return 1/2*l*b


class Rectangle:
    def __init__(self, length, breadth,):
        self.length = length
        self.breadth = breadth

    def area(self):
        return (self.length * self.breadth)

    def diagonal_length(self):
        return (((self.length)**2 + (self.breadth)**2)**0.5)

    def perimeter(self):
        return (2*(self.length+self.breadth))


# 3d figures
# what is done
# 1. cuboid
# 2. cylinder
# 3. cube
# 4. cone

class Cylinder:
    def __init__(self, r, h):
        self.radius = r
        self.height = h

    def lateral_surface_area(self):
        return 2*22/7*self.radius*self.height

    def total_surface_area(self):
        return 2*22/7*self.radius*(self.height+self.radius)

    def volume(self):
        return 22/7*(self.radius**2)*self.height


class Cuboid():
    def __init__(self, h, l, b):
        self.height = h
        self.lenght = l
        self.width = b

    def curved_surface_area(self):
        return 2*self.height*(self.lenght + self.width)

    def total_surface_area(self):
        return 2*(self.height*self.lenght+self.height*self.width+self.width*self.lenght)

    def volume(self):
        return self.height*self.width*self.lenght


class Cube():
    def __init__(self, side):
        self.a = side

    def lateral_surface_area(self):
        return 4*(self.a**2)

    def total_surface_area(self):
        return 6*(self.a**2)

    def volume(self):
        return self.a**3


class Cone():
    def __init__(self, height, radius, length=0):
        self.h = height
        if length == 0:
            self.l = math.sqrt(height**2 + radius**2)
        else:
            self.l = length
        self.r = radius

    def total_surface_area(self):
        return 22/7*self.l*self.r+22/7*(self.r**2)

    def lateral_surface_area(self):
        return 22/7*self.l*self.r

    def volume(self):
        return 22/7*(self.radius**2)*self.height*1/3
