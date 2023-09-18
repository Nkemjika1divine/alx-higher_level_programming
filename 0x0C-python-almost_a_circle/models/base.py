#!/usr/bin/python3
"""A Base Class"""
import json
import csv


class Base:
    """Setting up the class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Args:
        id = increments the class attribute if nothing is passed
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a JSON represebtation of a list of dictionaries"""
        if list_dictionaries is None:
            return json.dumps([])
        if type(list_dictionaries) == list:
            if len(list_dictionaries) == 0:
                return json.dumps([])
            else:
                return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes a json string representation of list_objs to a file"""
        if list_objs is None:
            files = []
        elif type(list_objs) is list:
            files = [i.to_dictionary() for i in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f:
            f.write(Base.to_json_string(files))

    @staticmethod
    def from_json_string(json_string):
        """returns a list of json string representation"""
        if json_string is None:
            return []
        if type(json_string) == str:
            if len(json_string) == 0:
                return []
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instnce with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                value = cls(5)
            if cls.__name__ == "Rectangle":
                value = cls(5, 8)
                value.update(**dictionary)
            return value

    @classmethod
    def load_from_file(cls):
        """loads json from a file"""
        filename = "{}.json".format(cls.__name__)
        obj = []
        if filename is True:
            with open(filename, "r") as f:
                line = f.readline()
                final_list = Base.from_json_string(line)
            for i in final_list:
                cc = cls.create(**i)
                obj.append(cc)
            return obj
