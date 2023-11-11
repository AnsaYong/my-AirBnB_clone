#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity

my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

my_state = State()
my_state.name = "New Jersey"
my_state.save()
print(my_state)

my_amenity = Amenity()
my_amenity.name = "Bathroom"
my_amenity.save()
print(my_amenity)
