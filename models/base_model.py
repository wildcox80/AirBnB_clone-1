#!/usr/bin/python3
"""base_model.py module"""
import uuid
from datetime import datetime


class BaseModel():
    """
    BaseModel class:
    ----------------
    It defines all common attributes/methods
    for the other classes.

    """

    def __init__(self, id=None):
        """
        This is the constructor.

        Arguments:
        ---------
        id [str] -- UUID generated with python uuid.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """str representation of the base class"""
        msg = ("[{}] ({}) {}".format(self.__class__.__name__,
               self.id, self.__dict__))
        return msg

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = dict(self.__dict__)
        new_dict["created_at"] = str(self.created_at.isoformat())
        new_dict["updated_at"] = str(self.updated_at.isoformat())
        new_dict["__class__"] = self.__class__.__name__
        return (new_dict)
