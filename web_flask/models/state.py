#!/usr/bin/python3

class State(BaseModel, Base):
    

    @property
    def cities(self):
        """Getter for cities if storage engine is not DBStorage"""
        from models import storage
        from models.city import City
        if not isinstance(storage, DBStorage):
            city_list = [city for city in storage.all(City).values() if city.state_id == self.id]
            return city_list
        return []
