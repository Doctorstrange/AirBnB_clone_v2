#!/usr/bin/python3
"""nstantiates an object of class FileStorage"""
import os


main_storage = os.getenv('HBNB_TYPE_STORAGE')


if main_storage == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()#!/usr/bin/python3
"""nstantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
