from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.activity import Activity
from models.concept import Concept
from models.option import Option
from models.quiz import Quiz
from models.resource import Resource
from os import getenv
from models.base_model import Base
import models

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
        env = getenv('env')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db))

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def all(self, cls=None):
        """
        query on the current database session and returns
        a dictionary of objects of a given class or all classes
        """
        obj_dict = {}
        if cls and cls in classes.values() or cls in classes.keys():
            for row in self.__session.query(classes[cls]).all():
                key = row.__class__.__name__ + '.' + row.id
                obj_dict[key] = row
                return obj_dict
        else:
            for clss in classes:
                    objs = self.__session.query(classes[clss]).all()
                    for row in objs:
                        key = row.__class__.__name__ + '.' + row.id
                        obj_dict[key] = row
            return (obj_dict)
    
    def new(self, obj):
        """ add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
    
    def close(self):
        """
        release the current session after a transaction for
        a future reload
        """
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values() or cls not in classes.keys():
            return None
        all_classes = models.storage.all(cls)
        for value in all_classes.values():
            if value.id == id:
                return value
        return None
    
    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        count = 0
        if cls and cls in classes.values or cls in classes.keys():
            count = len(models.storage.all(cls).values())
        else:
            count = len(models.storage.all().values())
        return count