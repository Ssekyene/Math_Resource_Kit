from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

QuizOption = Table('quiz_option', Base.metadata,
                   Column('quiz_id', String(60),
                          ForeignKey('quiz.id', onupdate='CASCADE', ondelete='CASCADE'),
                          primary_key=True),
                    Column('option_id', String(60),
                          ForeignKey('option.id', onupdate='CASCADE', ondelete='CASCADE'),
                          primary_key=True)
                   )

class Quiz(BaseModel, Base):
    """Representation of a quiz"""
    __tablename__ = 'quiz'
    correct_option = Column(String(15), nullable=False)
    concept_id = Column(String(60), ForeignKey('concept.id'), nullable=False)
    options = relationship('Option', secondary='quiz_option', backref='quizzes', viewonly=False)