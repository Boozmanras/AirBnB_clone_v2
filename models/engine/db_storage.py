#!/usr/bin/python3
"""Module for setting up and managing MySQL database storage with SQLAlchemy."""

import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """
    Manages interactions between the MySQL database and the application using SQLAlchemy.
    This class handles the creation of the database engine and session, 
    as well as database operations like querying, adding, and deleting objects.
    """

    # Dictionary mapping class names to their respective classes
    all_classes = {
        "BaseModel": BaseModel, 
        "User": User, 
        "State": State,
        "City": City, 
        "Amenity": Amenity, 
        "Place": Place,
        "Review": Review
    }
    
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the DBStorage instance by creating the engine 
        and optionally dropping all tables if in a testing environment.
        """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                os.environ['HBNB_MYSQL_USER'],
                os.environ['HBNB_MYSQL_PWD'],
                os.environ['HBNB_MYSQL_HOST'],
                os.environ['HBNB_MYSQL_DB']
            ), 
            pool_pre_ping=True
        )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries all objects in the current database session, 
        optionally filtered by class.

        Args:
            cls (str, optional): The class name to filter by.

        Returns:
            dict: A dictionary of objects with the format <class name>.<id>.
        """
        obj_dict = {}
        if cls:
            cls = self.all_classes[cls]
            objects = self.__session.query(cls).all()
        else:
            objects = self.__session.query(
                State, City, User, Amenity, Place, Review
            ).all()
        for obj in objects:
            key = f"{obj.__class__.__name__}.{obj.id}"
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """
        Adds a new object to the current database session.

        Args:
            obj (BaseModel): The object to be added.
        """
        self.__session.add(obj)
        self.__session.flush()

    def save(self):
        """
        Commits all changes made in the current database session to the database.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the current database session, if provided.

        Args:
            obj (BaseModel, optional): The object to be deleted. If None, no action is taken.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database (if they don't exist) 
        and initializes a new database session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Closes the current database session.
        """
        self.__session.close()
