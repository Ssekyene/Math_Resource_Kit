from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Text
from datetime import datetime
import uuid
import models

Base = declarative_base()
fmt = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    id = Column(String(60), primary_key=True)
    descritption = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""

        if kwargs and kwargs != {}:
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)
            if kwargs.get('created_at', None) and type(self.created_at) is str:
                    self.created_at = datetime.strptime(kwargs['created_at'], fmt)
            else:
                self.created_at = datetime.now()
            if kwargs.get('updated_at', None) and type(kwargs['updated_at'] is str):
                self.updated_at = datetime.strptime(kwargs['updated_at'], fmt)
            else:
                self.updated_at = datetime.now()
            if kwargs.get('id', None) is None:
                self.id = str(uuid.uuid4())
        
        else:    
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)

    def save(self):
        """
        updates the attribute 'updated_at' with the current
        datetime and saves to the database
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
            """delete the current instance from the storage"""
            storage.delete(self)

    def to_dict(self):
            """returns a dictionary containing all keys/values of the instance"""
            new_dict = self.__dict__.copy()
            if "created_at" in new_dict:
                new_dict["created_at"] = new_dict["created_at"].strftime(fmt)
            if "updated_at" in new_dict:
                new_dict["updated_at"] = new_dict["updated_at"].strftime(fmt)
            new_dict["__class__"] = self.__class__.__name__
            if "_sa_instance_state" in new_dict:
                del new_dict["_sa_instance_state"]
            return new_dict