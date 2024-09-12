from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table

QuizOption = Table('quiz_option', Base.metadata,
                   Column('quiz_id', String(60),
                          ForeignKey('quiz', onupdate='CASCADE', ondelete='CASCADE'),
                          primary_key=True),
                    Column('option_id', String(60),
                          ForeignKey('option', onupdate='CASCADE', ondelete='CASCADE'),
                          primary_key=True)
                   )

class Quiz(BaseModel, Base):
    """Representation of a quiz"""
    __tablename__ = 'quiz'
    correct_option = Column(String(12), nullable=False)
    concept_id = Column(String(60), ForeignKey('concept'), nullable=False)