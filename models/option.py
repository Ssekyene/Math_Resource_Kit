from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Option(BaseModel, Base):
    """Representation of a option"""
    __tablename__ = 'option'
    identifier = Column(String(15), nullable=False, unique=True)