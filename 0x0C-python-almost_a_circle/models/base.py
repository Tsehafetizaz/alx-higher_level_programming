#!/usr/bin/python3
"""
Module for the Base class.
"""

import csv
import json
import os


class Base:
    """
    Base class for other classes in the project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.
        Args:
            id (int): The id of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = "{}.json".format(cls.__name__)
        list_dicts = (
            [obj.to_dictionary() for obj in list_objs] if list_objs else []
        )
        json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json_string.
        Args:
            json_string (str): A string representing a list of dictionaries.
        Returns:
            list: The list represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set.
        Args:
            **dictionary: A double pointer to a dictionary.
        Returns:
            An instance with attributes set as per dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from a JSON file.
        Returns:
            list: A list of instances.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            list_dicts = cls.from_json_string(file.read())

        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize a list of objects to a CSV file.
        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', newline='') as csvfile:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize a list of objects from a CSV file.
        Returns:
            list: A list of instances.
        """
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []

        with open(filename, 'r', newline='') as csvfile:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.___name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']

            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            list_dicts = [row for row in reader]

            # Converting string values to integers where necessary
            for d in list_dicts:
                for key, value in d.items():
                    d[key] = int(value)

            return [cls.create(**d) for d in list_dicts]
