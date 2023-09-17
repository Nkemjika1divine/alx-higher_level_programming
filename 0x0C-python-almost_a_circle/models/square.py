#!/usr/bin/python3
"""A Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Setting up a class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Args:
        All inherited from the super class.
        size covers the height and width being equal
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the height and width of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the height and width of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns a string representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """updates the square attributes using args and kwargs"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                    self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                if key == "id":
                    self.id = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
    
    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
