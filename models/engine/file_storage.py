#!/usr/bin/python3
"""file_storage.py module"""
import json
from models.base_model import BaseModel


class FileStorage():
    """
    FileStorage class:
    ------------------
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        public instance method that returns the
        dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        public instance method that sets in __objects
        the obj with key <obj class name>.id

        Variables:
        ----------
        key [str] -- key format generated.
        """
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """
        public instance method that serializes __objects
        to the JSON file (path: __file_path).

        Variables:
        ----------
        new_dict [dict] -- keys and values to build JSON.
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            if isinstance(value, dict):
                new_dict[key] = value
            else:
                new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """
        public instance method that deserializes a JSON
        file to __objects.
        """
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                new_dict = json.load(my_file)

            for key, value in new_dict.items():
                FileStorage.__objects[key] = BaseModel(**value)

        except FileNotFoundError:
            pass
