from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, Table, ForeignKey
from sqlachemy.orm import relationship

ConceptResource = Table('concept_resource', Base.metadata,
                        Column('concept_id', String(60),
                                ForeignKey('concept', onupdate='CASCADE', ondelete='CASCADE'),
                                primary_key=True),
                        Column('resource_id', String(60),
                                ForeignKey('resource', onupdate='CASCADE', ondelete='CASCADE'),
                                primary_key=True)
                        )

class Concept(BaseModel, Base):
    """Representation of concept """

    __tablename__ = 'concept'
    name = Column(String(1024), nullable=False)
    introduction = Column(Text, nullable=False)
    conclusion = Column(Text)
    quizzes = relationship('Quiz', backref='concept', casecade='all delete delete-orphan')
    activities = relationship('Activity', backref='concept', cascade='all delete delete-orphan')
    resources = relationship('Resource', secondary='ConceptResource', backref='concepts', viewonly=False)