#!/usr/bin/python3
import json
import os
import models
from datetime import datetime

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        obj_dict = {}

        for key, value in obj.__dict__.items():
            if isinstance(value, datetime):
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value
        obj_dict['__class__'] = obj.__class__.__name__

        key_str = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key_str] = obj_dict

    def save(self):
        """
        Serialize python dictionary - stored in the class attribute `__objects`
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """
        Deserialize json file and return it to the dictionary
        """
        file_exists = os.path.exists(FileStorage.__file_path)
        if file_exists:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
