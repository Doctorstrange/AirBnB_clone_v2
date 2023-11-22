#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """test the console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.shared_instance = HBNBCommand()

    def test_create(self):
        """Test create command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.shared_instance.onecmd("create qwerty")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.shared_instance.onecmd('create User email="user" password="passwd"')
        with patch('sys.stdout', new=StringIO()) as f:
            self.shared_instance.onecmd("all User")
            self.assertEqual(
                "[\"[User", f.getvalue()[:7])


if __name__ == "__main__":
    unittest.main()