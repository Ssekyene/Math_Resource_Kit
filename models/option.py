from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text

class Option(BaseModel, Base):
    """Representation of a option"""
    __tablename__ = 'option'