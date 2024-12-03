import turtle
from copy import copy, deepcopy

class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point ({self.x}, {self.y})'

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def translated(self, dx=0, dy=0):
        point = copy(self)
        point.translate(dx, dy)
        return point

    def translated_v2(self, dx=0, dy=0):
        x = self.x + dx
        y = self.y + dy
        return Point(x, y)


class Line:
    def __init__(self, p1, p2, t:turtle.Turtle=None):
        self.t = t if t else turtle.Turtle()
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f'Line ({self.p1}, {self.p2})'

    #Exercise 16.10.02
    def __eq__(self, other):
        return (self.p1 == other.p1 and self.p2 == other.p2) or (self.p1 == other.p2 and self.p2 == other.p1)

    def jumpto(self):
        self.t.penup()
        self.t.goto(self.p1.x, self.p1.y)
        self.t.pendown()

    def draw(self):
        self.jumpto()
        self.t.goto(self.p2.x, self.p2.y)

    #Exercise 16.10.03
    def midpoint(self) -> Point: #don't know how the '->' thing works but ok
        return Point((self.p1.x + self.p2.x)/2, (self.p1.y + self.p2.y)/2) #math that I apparently cannot come up with by myself.
    #copied yours, original version didn't work at all lol

class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """

    def __init__(self, width, height, corner:Point, t:turtle.Turtle=None):
        self.t = t if t else turtle.Turtle()
        self.width = width
        self.height = height
        self.corner = corner

    def __str__(self):
        return f'Rectangle({self.width}, {self.height}, {self.corner})'

    def make_points(self):
        p1 = self.corner
        p2 = p1.translated(self.width, 0)
        p3 = p2.translated(0, self.height)
        p4 = p3.translated(-self.width, 0)
        return p1, p2, p3, p4

    def make_lines(self):
        p1, p2, p3, p4 = self.make_points()
        return Line(p1, p2), Line(p2, p3), Line(p3, p4), Line(p4, p1)

    def draw(self):
        lines = self.make_lines()
        for line in lines:
            line.draw()

    def grow(self, dwidth, dheight):
        self.width += dwidth
        self.height += dheight

    def translate(self, dx, dy):
        self.corner.translate(dx, dy)

    #Exercise 16.10.04
    def midpoint(self) -> Point:
        return Point((self.corner.x + self.width.x)/2, (self.corner.y + self.width.y)/2)#also math that I apparently
                                                                                        #can't come up with myself

    #Exercise 16.10.05
    def make_cross(self) -> list[Line]: #pointer thing that I don't understand
        cross_lines = [] #initializes list to be returned
        lines = self.make_lines() #initializes lines
        mp1 = mp2 = 0 #initializes mp1, mp2 to 0
        for l, line in enumerate(lines): #iterates through lines
            if l == 0: #for the first case,
                mp1 = line.midpoint() #calculate a midpoint
            if l == 1: #for the second case,
                mp2 = line.midpoint() #calculate another midpoint
            if l == 2: #for the third case,
                cross_lines.append(Line(mp1, line.midpoint(), t=self.t)) #append a midpoint and something that I'm not comprehending
            if l == 3: #for the fourth case,
                cross_lines.append(Line(mp2, line.midpoint(), t=self.t)) #ditto
        return cross_lines #return the list of things

class Circle: #Exercise 16.10.06
    def __init__(self, radius:float, center:Point, t:turtle.Turtle=None):
        self.radius = radius
        self.center = center
        self.t = t if t else turtle.Turtle()

    def __str__(self):
        return f'Circle ({self.center}, {self.radius}).'

    def draw(self):
        start_y = self.center.y - self.radius
        self.t.penup()
        self.t.goto(self.center.x, start_y)
        self.t.pendown()
        turtle.circle(self.radius)



start = Point(0, 0)
end1 = copy(start)
end1.translate(300, 0)
line1 = Line(start, end1)

end2 = start.translated(0, 150)
line2 = Line(start, end2)

corner = Point(30, 20)
box1 = Rectangle(100, 50, corner)
box2 = copy(box1)
box2.grow(60, 40)
box2.translate(30, 20)

corner = Point(20, 20)
box3 = Rectangle(100, 50, corner)
box4 = deepcopy(box3)
box3.translate(50, 30)
box4.grow(100, 60)

shapes = [line1, line2, box3, box4]

for shape in shapes:
    shape.draw()

input('Press any key to exit the program.')

