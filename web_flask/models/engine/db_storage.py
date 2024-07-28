#!/usr/bin/python3

class DBStorage:

    def close(self):
        """Call remove() method on the private session attribute (self.__session)"""
        self.__session.remove()
