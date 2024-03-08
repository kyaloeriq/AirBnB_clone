#!/usr/bin/python3
"""The FileStorage class"""
import os
import json
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place

class FileStorage:
    """A representation of an abstracted storage engine

    Attributes:
    __file_path (str): Name of the file to save Objects to
    __objects (dict): Instantiated objects"""
    __file_path = "file.json"
    __objects = {}
    classes = ["BaseModel", "User", "State",
               "City", "Amenity", "Place", "Review"]

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """De-serialize the JSON file __file_path to __objects, if it exists."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "User":
                        cls = User
                    else:
                        cls = eval(class_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
