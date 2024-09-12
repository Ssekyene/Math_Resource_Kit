from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Resource(BaseModel, Base):
    """Representation of a resource"""
    __tablename__ = 'resource'
    url = Column(String(1024), nullable=False)
