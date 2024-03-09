#!/usr/bin/python3
"""The FileStorage class"""
import os
import json

class FileStorage:
    """A class for serializing instances to a JSON file and deserializing JSON file to instances."""

    __file_path = "file.json"
    __objects = {}


    @classmethod
    def all(cls):
        """Returns the dictionary __objects"""
        return cls.__objects

    @classmethod
    def new(cls, obj):
        """Sets in __objects obj with key <obj class name>.id."""
        key = f"{type(obj).__name__}.{obj.id}"
        cls.__objects[key] = obj

    @classmethod
    def save(cls):
        """Serializes __objects to the JSON file __file_path."""
        serialized_objects = {}
        for key, obj in cls.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(cls.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

     @classmethod
     def reload(cls):
        """De-serializes JSON file __file_path to __objects, if it exists"""
        if os.path.exists(cls.__file_path):
            with open(cls.__file_path, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    print("Error: JSON file is corrupted.")
                    return
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    try:
                        cls_ = getattr(__import__('models.' + class_name.lower()), class_name)
                    except AttributeError:
                        print(f"Error: Class {class_name} not found.")
                        continue
                    obj = cls_(**value)
                    cls.__objects[key] = obj
