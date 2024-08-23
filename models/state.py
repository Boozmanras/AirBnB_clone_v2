#!/usr/bin/python3
"""Module defining the State class for representing states in the system."""

import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Represents a state in the database.
    
    Attributes:
        __tablename__ (str): The name of the table in the database.
        name (str): The name of the state.
        cities (relationship): A relationship with the City class, 
                               representing all cities associated with this state.
    """

    __tablename__ = 'states'
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', back_populates='state',
            cascade='all, delete, delete-orphan'
        )
    else:
        name = ""

        @property
        def cities(self):
            """
            Retrieves all city instances associated with this state.
            
            Returns:
                list: A list of City objects where the `state_id` matches the state's `id`.
            """
            cities_instances = []
            cities_dict = models.storage.all(models.City)
            for key, value in cities_dict.items():
                if self.id == value.state_id:
                    cities_instances.append(value)
            return cities_instances
