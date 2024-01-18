#!/usr/bin/python3
"""Defines a rectangle"""

import json


class Base:
    """Creates a class named base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts list of dictionaries into json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the objects in a file"""
        if list_objs is None:
            return []

        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            json_string = cls.to_json_string
            ([obj.__dict__ for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Reads a JSON string and returns a list of objects"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(dictionary.get('size', 1))
        else:
            raise ValueError("Unsupported class")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Loads data from a file to create instances"""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dict_list = cls.from_json_string(json_string)
                return [cls.create(**dictionary) for dictionary in dict_list]

        except FileNotFoundError:
            return []
