#!/usr/bin/python3
"""Defines the FileStorage class for managing storage of AirBnB models."""
import json
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Handles the serialization of instances to a JSON file and 
    the deserialization of JSON files back into instances.

    Attributes:
        __file_path (str): Path to the JSON file used for storage.
        __objects (dict): Dictionary to store all objects by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects, optionally filtered by class.

        Args:
            cls (class, optional): The class type to filter by.

        Returns:
            dict: A dictionary of objects of the specified class, or all objects if no class is specified.
        """
        if cls is None:
            return self.__objects
        else:
            filtered_dict = {}
            for key, value in self.__objects.items():
                if isinstance(cls, str):
                    if cls == key.split('.')[0]:
                        filtered_dict[key] = value
                else:
                    if isinstance(value, cls):
                        filtered_dict[key] = value
            return filtered_dict

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj (BaseModel): The object to be added to the storage.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializes the current state of objects to the JSON file specified in __file_path.
        """
        objects_dict = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """
        Deserializes the JSON file specified in __file_path to reload stored objects.
        If the file does not exist, no exception is raised.
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in json.load(f).items():
                    cls_name = value["__class__"]
                    self.__objects[key] = eval(cls_name)(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Removes an object from the storage dictionary, if it exists.

        Args:
            obj (BaseModel, optional): The object to be removed. If None, nothing is deleted.
        """
        if obj:
            key_to_delete = ""
            for key, value in self.__objects.items():
                if obj == value:
                    key_to_delete = key
                    break
            if key_to_delete:
                del self.__objects[key_to_delete]

    def close(self):
        """
        Calls the reload method to load stored objects from the JSON file.
        """
        self.reload()
