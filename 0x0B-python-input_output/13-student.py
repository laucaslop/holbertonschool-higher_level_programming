#!/usr/bin/python3
""" Module """


class Student:
    """ Class Student """

    def __init__(self, first_name, last_name, age):
        """Initializes Student object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary """

        new_dict = {}
        if type(attrs) is list and all(type(i) is str for i in attrs):
            for att in attrs:
                if att in self.__dict__:
                    new_dict[att] = self.__dict__[att]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key in json:
            self.__dict__[key] = json[key]
