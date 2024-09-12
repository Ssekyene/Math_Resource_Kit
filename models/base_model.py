from sqlalchemy.ext.declarative import declarative_base
from sqlachemy import Column, String, DateTime, Text
from datetime import datetime

Base = declarative_base()

class BaseModel:
    id = Column(String(60), primary_key=True)
    descritption = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

