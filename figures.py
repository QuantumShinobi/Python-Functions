import math


# 2d figs
# 1. square
# 2. rectangle
# 3. triangle
# 4. rhombus
# 5. circle
class Square():
    def __init__(self, side,):
        self.side = side

    def area(self):
        return (self.side**2)

    def perimeter(self):
        return (4*self.side)

    def diagonal(self):
        return ((2**0.5)*self.side)


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


class Rhombus():
    def perimeter(self):
        l = float(input("Enter the 1st side"))
        b = float(input("Enter the 2nd side"))
        return 2*(l+b)

    def area(self):
        l = float(input("Enter the 1st daigonal"))
        b = float(input("Enter the 2nd daigonal"))
        return 1/2*l*b


class Circle():
    def __init__(self, r):
        self.radius = r

    def circumfrence(self):
        return 22/7*self.radius * 2

    def area(self):
        return 22/7 * (self.radius**2)


class Triangle():
    def __init__(self):
        pass

    def area(self):
        method = int(input('''
how do u want to calculate the area
1) b * h * 1/2
2) heron's formula
        '''))
        if method == 2:
            side1 = float(input('Enter the side'))
            side2 = float(input('Enter the side'))
            side3 = float(input('Enter the side'))
            s = (side1 + side2 + side3) / 2
            return (s * (s - side1) * (s - side2) * (s - side3))**0.5

        else:
            base = float(input('Enter the base'))
            height = float(input('Enter the height'))
            return 1 / 2 * base * height

    def perimeter(self):
        side1 = float(input('Enter the side'))
        side2 = float(input('Enter the side'))
        side3 = float(input('Enter the side'))
        return side1 + side2 + side3


# 3d figures
# what is done
# 1. cuboid
# 2. cylinder
# 3. cube
# 4. cone
# 5. sphere
# 6. hemisphere
class Cube():
    def __init__(self, side):
        self.a = side

    def lateral_surface_area(self):
        return 4*(self.a**2)

    def total_surface_area(self):
        return 6*(self.a**2)

    def volume(self):
        return self.a**3


class Cuboid():
    def __init__(self, height, length, breadth):
        self.height = height
        self.lenght = length
        self.width = breadth

    def curved_surface_area(self):
        return 2*self.height*(self.lenght + self.width)

    def total_surface_area(self):
        return 2*(self.height*self.lenght+self.height*self.width+self.width*self.lenght)

    def volume(self):
        return self.height*self.width*self.lenght


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


class Sphere():
    def __init__(self, radius):
        self.r = radius

    def surface_area(self):
        return 4*22/7*(self.r**2)

    def volume(self):
        return 4/3*22/7*(self.r**3)


class HemiSphere():
    def __init__(self, radius, diameter=0):
        self.r = radius
        if diameter == 0:
            self.d = 2*radius
        else:
            self.d = diameter

    def total_surface_area(self):
        return 3*22/7*(self.r**2)

    def lateral_surface_area(self):
        return 2*22/7*(self.r**2)

    def volume(self):
        return 4/3*22/7*(self.r**3)
