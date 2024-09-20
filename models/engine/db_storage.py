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
import difflib

classes = {"Concept": Concept, "Activity": Activity,
           "Option": Option, "Quiz": Quiz, "Resource": Resource}

class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        user = getenv('MRK_MYSQL_USER')
        pwd = getenv('MRK_MYSQL_USER_PWD')
        host = getenv('MRK_MYSQL_HOST')
        db = getenv('MRK_MYSQL_DB')
        env = getenv('MRK_ENV')
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
            try:
                # converting the Class name to a string
                if issubclass(cls, Base):
                    cls = str(cls.__name__)
            except:
                pass
            objs = self.__session.query(classes[cls]).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                obj_dict[key] = obj
            return obj_dict
        else:
            for clss in classes:
                    objs = self.__session.query(classes[clss]).all()
                    for obj in objs:
                        key = obj.__class__.__name__ + '.' + obj.id
                        obj_dict[key] = obj
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
        try:
            # converting the Class name to a string
            if issubclass(cls, Base):
                cls = str(cls.__name__)
        except:
            pass
        
        if cls not in classes.keys():
            return None
        all_classes = models.storage.all(cls)
        for value in all_classes.values():
            if value.id == id:
                return value
        return None
    

    def get_by_name(self, cls, name):
        """
        Returns an object based on its Class and name attribute, or
        None if not found
        """
        try:
            # converting the Class name to a string
            if issubclass(cls, Base):
                cls = str(cls.__name__)
        except:
            pass
        if cls not in classes.keys():
            return None
        all_objs = models.storage.all(cls).values()
        for obj in all_objs:
            try:
                if obj.name == name:
                    return obj
            except AttributeError:
                print("Object has no name attribute!")
        return None
    
    def concept_search(self, keyword):
        """
        Returns a list concept objects based on the keyword
        or nothing if no concept name matched
        """
        concept_objs = models.storage.all(Concept).values()
        keyword = keyword.lower()
        matched_concepts = []
        for obj in concept_objs:
            name = obj.name.lower()
            similarity_ratio = difflib.SequenceMatcher(None, keyword, name).ratio()
            if keyword in name or similarity_ratio > 0.7: # 70% similarity or more
                matched_concepts.append(obj)
        return matched_concepts      

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
