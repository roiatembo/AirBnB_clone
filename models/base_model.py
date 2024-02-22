#!/usr/bin/python3
"""This script is the base model"""

from datetime import datetime
import uuid

class BaseModel:
    """
    BaseModel class defines common attributes and methods for other classes.

    Public instance attributes:
    - id: string - a unique identifier for each instance, assigned using uuid.uuid4()
    - created_at: datetime - the date and time when an instance is created
    - updated_at: datetime - the date and time when an instance is last updated

    Public instance methods:
    - save(): updates the updated_at attribute with the current datetime
    - to_dict(): returns a dictionary containing all instance attributes
                 with class name, created_at, and updated_at converted to string objects in ISO format
    """

    def __init__(self):
        """
        Initializes a new instance of BaseModel.

        Sets the id attribute to a unique identifier using uuid.uuid4(),
        and sets the created_at and updated_at attributes to the current datetime.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.

        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Includes all instance attributes with class name, created_at,
        and updated_at converted to string objects in ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

