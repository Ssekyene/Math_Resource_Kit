from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Activity(BaseModel, Base):
    """Represents an activity(of integration)"""
    __tablename__ = 'activity'
    concept_id = Column(String(60), ForeignKey('concept'), nullable=False)