from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.activity import Activity
from models.concept import Concept
from models.option import Option
from models.quiz import Quiz
from models.resource import Resource
from os import getenv
from models.base_model import Base

classes = {"Concept": Concept, "Activity": Activity,
           "Option": Option, "Quiz": Quiz, "Resource": Resource}

class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        user = getenv('user')
        pwd = getenv('pwd')
        host = getenv('host')
        db = getenv('db')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db))

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)