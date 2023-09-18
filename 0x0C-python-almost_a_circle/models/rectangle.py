#!/usr/bin/python3
"""A Rectangle Module"""
import turtle
from models.base import Base


class Rectangle(Base):
    """Setting up the class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Args:
        width = widtg of the rectangle
        height = height of the rectangle
        x
        y
        id = inherited from the class Base
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle based on certain parameters"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle based on certain parameters"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x based on certain parameters"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y based on certain parameters"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """returns a represemtation of the rectangle using " " and "#" chars"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """returns a atring representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} -"\
            " {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """sets the values of the constructor using args and kwargs"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "height":
                    self.height = value
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of the rectangle"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }

    @staticmethod
    def draw(list_rectangles, list_squares):
        """drawing rectangles and squares with the turtle module"""
        screen = turtle.Screen()
        draw = turtle.Turtle()

        screen.setup(width=50, height=50)

        screen.bgcolor("white")
        draw.pensize(5)
        draw.shape("turtle")

        draw.color("red")

        for i in list_rectangles:
            draw.showturtle()
            draw.up()
            draw.goto(i.x, i.y)
            draw.down()
            for j in range(2):
                draw.forward(i.width)
                draw.left(90)
                draw.forward(i.height)
                draw.left(90)
            draw.hideturtle()

        draw.color("blue")

        for i in list_squares:
            draw.showturtle()
            draw.up()
            draw.goto(i.x, i.y)
            draw.down()
            for j in range(2):
                draw.forward(i.size)
                draw.left(90)
                draw.forward(i.size)
                draw.left(90)
            draw.hideturtle()
        
        turtle.exitonclick()
