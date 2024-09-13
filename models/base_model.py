from sqlalchemy.ext.declarative import declarative_base
from sqlachemy import Column, String, DateTime, Text
from datetime import datetime
import uuid

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

    if kwargs and kwargs != []:
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
        if kwargs.get('description', None) is None:
            self.description = "Missing content"
    else:    
        self.id = str(uuid.uuid4())
        self.description = "Missing content"
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

def __str__(self):
    """String representation of the BaseModel class"""
    return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)