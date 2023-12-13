#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            filtered_objects = {}
            for key, obj in FileStorage.__objects.items():
                if isinstance(obj, cls):
                    filtered_objects[key] = obj
            return filtered_objects
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel

        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.__objects[key] = BaseModel(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects if it's inside"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del FileStorage.__objects[key]

    def close(self):
        """Deserialize JSON file to objects"""
        self.reload()
