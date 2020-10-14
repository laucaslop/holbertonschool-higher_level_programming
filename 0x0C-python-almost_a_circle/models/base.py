#!/usr/bin/python3
""" Base module """
import json
import csv


class Base:
    """ Class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initial """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns JSON strings in list """
        if type(json_string) != str or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attrs already set """
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
        if cls.__name__ == "Square":
            tmp = cls(1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes to file with JSON string """
        with open(cls.__name__ + ".json", mode="w") as write_file:
            if list_objs is None:
                write_file.write("[]")
            else:
                write_file.write(cls.to_json_string(
                                 [item.to_dictionary() for item in list_objs]))

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        tmp = []
        with open(cls.__name__ + ".json", mode="r") as read_file:
            text = read_file.read()
        text = cls.from_json_string(text)
        for item in text:
            if type(item) == dict:
                tmp.append(cls.create(**item))
            else:
                tmp.append(item)
        return tmp

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves to csv file """
        tmp = [item.to_dictionary() for item in list_objs]
        with open(cls.__name__ + ".csv", mode="w") as save_file:
            write_to = csv.DictWriter(save_file, tmp[0].keys())
            write_to.writeheader()
            write_to.writerows(tmp)

    @classmethod
    def load_from_file_csv(cls):
        """ Loads from csv file """
        tmp = []
        tmp_dict = {}
        with open(cls.__name__ + ".csv", mode="r") as read_file:
            read_from = csv.DictReader(read_file)
            for item in read_from:
                for k, v in dict(item).items():
                    tmp_dict[k] = int(v)
                tmp.append(clls.create(**tmp_dict))
        return tmp
