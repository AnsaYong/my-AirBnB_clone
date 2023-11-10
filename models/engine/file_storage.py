#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from datetime import datetime

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key_str = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key_str] = obj

    def save(self):
        """
        Serialize python dictionary - stored in the class attribute `__objects`
        """
        obj_dict ={}

        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
                json.dump(obj_dict, f)

    def reload(self):
        """
        Deserialize json file and return it to the dictionary
        """
        file_exists = os.path.exists(FileStorage.__file_path)
        if file_exists:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
                for val in FileStorage.__objects.values():
                    class_name = val["__class__"]
                    if isinstance(class_name, str) and type(eval(class_name)) == type:
                        self.new(eval(class_name)(**val))
