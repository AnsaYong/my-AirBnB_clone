#!/usr/bin/python3
import uuid
from datetime import datetime, timedelta

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        updated_dict = {}

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                updated_dict[key] = value.isoformat()
            else:
                updated_dict[key] = value

        updated_dict['__class__'] = self.__class__.__name__

        return updated_dict
