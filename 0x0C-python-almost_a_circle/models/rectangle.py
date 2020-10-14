#!/usr/bin/python3
""" Rectangle module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initial """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter """
        return self.__width

    @property
    def height(self):
        """ Getter """
        return self.__height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @width.setter
    def width(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Area """
        return self.__height * self.__width

    def display(self):
        """ Prints in stdout the Rectangle
        instance with the character # """
        print('\n' * self.__y, end='')
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """ Update class rectangle """

        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id,
                                                self.__x,
                                                self.__y,
                                                self.__width,
                                                self.__height)

    def update(self, *args, **kwargs):
        """ Assigns an argument """
        if len(kwargs) is not 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif len(args) is not 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except:
                pass
        else:
            print()

    def to_dictionary(self):
            """ Returns the dictionary
            representation of a Rectangle """
            return {'x': self.__x, 'y': self.__y, 'id': self.id,
                    'height': self.__height, 'width': self.__width}
