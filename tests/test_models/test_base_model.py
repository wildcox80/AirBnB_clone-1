#!/usr/bin/python3
"""Module for test BaseModel class"""
import unittest
import json
import pep8
import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class"""

    def test_doc_module(self):
        """Module documentation"""
        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_base_model(self):
        """Test that models/base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base_model(self):
        """Test that tests/test_models/test_base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_first_task(self):
        """Test creation of class"""
        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.my_number, 89)
        model_types_json = {
            "my_number": int,
            "name": str,
            "__class__": str,
            "updated_at": str,
            "id": str,
            "created_at": str
        }
        my_model_json = my_model.to_dict()
        for key, value in model_types_json.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, my_model_json)
                self.assertIs(type(my_model_json[key]), value)

    def test_base_types(self):
        second_model = BaseModel()
        self.assertIs(type(second_model), BaseModel)
        second_model.name = "Andres"
        second_model.my_number = 80
        self.assertEqual(second_model.name, "Andres")
        self.assertEqual(second_model.my_number, 80)
        model_types = {
            "my_number": int,
            "name": str,
            "updated_at": datetime.datetime,
            "id": str,
            "created_at": datetime.datetime
            }
        for key, value in model_types.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, second_model.__dict__)
                self.assertIs(type(second_model.__dict__[key]), value)

if __name__ == '__main__':
    unittest.main()
