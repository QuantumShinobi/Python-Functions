class circle():
    def __init__(self, r):
        self.radius = r

    def circumfrence(self):
        return 22/7*self.radius * 2

    def area(self):
        return 22/7 * (self.radius**2)


class rhombus():
    def perimeter(self):
        l = float(input("Enter the 1st side"))
        b = float(input("Enter the 2nd side"))
        return 2*(l+b)

    def area(self):
        l = float(input("Enter the 1st daigonal"))
        b = float(input("Enter the 2nd daigonal"))
        return 1/2*l*b


class rectangle:
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


class cylinder:
    def __init__(self, r, h):
        self.radius = r
        self.height = h

    def lateral_surface_area(self):
        return 2*22/7*self.radius*self.height

    def total_surface_area(self):
        return 2*22/7*self.radius*(self.height+self.radius)
