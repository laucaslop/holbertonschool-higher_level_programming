#!/usr/bin/python3
""" Square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initial """

        super().__init__(id=id, x=x, y=y, width=size, height=size)

    @property
    def size(self):
        """ Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Getter"""
        self.width = value
        self.height = value

    def __str__(self):
        """ Update the class Square """

        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.width)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if len(kwargs) is not 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif len(args) is not 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]

            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
            """ Returns the dictionary
            representation of a Rectangle """
            return {'id': self.id, 'x': self.x,
                    'size': self.width, 'y': self.y}
