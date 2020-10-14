#!/usr/bin/python3
import unittest
import pep8
import json
import sys
import io
from models import base
from models.base import Base


class TestBaseDocs(unittest.TestCase):
    """ Check for documentation """
    def test_module_doc(self):
        """ Check for module documentation """
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """ Check for class documentation """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method_docs(self):
        """ Check for method documentation """
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)


class TestBasePep8(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ Test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base.py'
        file2 = 'tests/test_models/test_base.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestBase(unittest.TestCase):
    """ Tests for class Base """
    @classmethod
    def setUpClass(cls):
        """ Set up instances for tests """
        Base._Base__nb_objects = 0
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base(98)
        cls.b4 = Base()
        cls.b5 = Base("five")
        cls.b6 = Base(6.6)

    def test_id(self):
        """ Test id attribute """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 98)
        self.assertEqual(self.b4.id, 3)
        self.assertEqual(self.b5.id, "five")
        self.assertEqual(self.b6.id, 6.6)

    def test_to_json(self):
        """ Test to_json_string method """
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')
        d1 = {"width": 1, "height": 2, "x": 3, "y": 4, "id": 5}
        json_test = Base.to_json_string(d1)
        self.assertTrue(type(json_test) is str)
        test_dict = json.loads(json_test)
        self.assertEqual(test_dict, d1)

    def test_from_json(self):
        """ Test from_json_string method """
        self.assertEqual(Base.from_json_string([]), [])
        self.assertEqual(Base.from_json_string(None), [])
