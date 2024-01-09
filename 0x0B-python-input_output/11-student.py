#!/usr/bin/python3
"""Defines a student by first name, last name"""


class Student:
    """
    Defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiates a new Student object.
        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student.
        Args:
            attrs (list): Attributes to include in the dictionary.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces attributes of the Student instance.
        Args:
            json (dict): A dictionary with new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
