#!/usr/bin/python3
import json

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
        Serialize python dictionary
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.all(), f)

    def reload(self):
        """
        Deserialize json file
        """
        if FileStorage.__file_path:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
