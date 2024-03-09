#!/usr/bin/python3
"""The BaseModel"""
import models
import uuid
from datetime import datetime

class BaseModel:
    """Model for common methods/attributes"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def save(self):
        """Update updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
