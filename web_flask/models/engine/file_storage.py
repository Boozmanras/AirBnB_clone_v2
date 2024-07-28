#!/usr/bin/python3

class FileStorage:
    # ... other methods

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()
