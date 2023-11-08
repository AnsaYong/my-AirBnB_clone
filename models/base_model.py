#!/usr/bin/python3
import uuid
import models
from datetime import datetime, timedelta

class BaseModel:
    def __init__(self, *args, **kwargs):
        str_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            # Not a new instance (from a dictionary representation)
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at" and isinstance(value, str):
                        value = datetime.strptime(value, str_format)
                    setattr(self, key, value)
        else:
            #  A new instance (not from a dictionary representation)
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

            # In addition to the above attributes, load the previous attributes
            #stored_objects = models.storage.all()
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        updated_dict = {}

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                updated_dict[key] = value.isoformat()
            else:
                updated_dict[key] = value

        updated_dict['__class__'] = self.__class__.__name__

        return updated_dict
