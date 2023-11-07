#!/usr/bin/python3
"""
Test module for the ``BaseModel`` class.
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    description
    """
    def set_up(self):
        """
        Create an instance of the BaseModel class before each test
        """
        self.base = BaseModel()

    def test_id_string(self):
        """
        description
        """
        base = BaseModel()
        self.assertTrue(isinstance(base.id, str))
