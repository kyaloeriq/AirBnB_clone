#!/usr/bin/python3
"""The FileStorage class"""
import os
import json


class FileStorage:
    """A class serializing instances to JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects obj with key <obj class name>.id."""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes JSON file __file_path to __objects if it exists"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    try:
                        cls_ = globals()[class_name]
                    except KeyError:
                        print(f"Error: Class {class_name} not found.")
                        continue
                    obj = cls_(**value)
                    self.__objects[key] = obj
