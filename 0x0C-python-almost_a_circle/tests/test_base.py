#!/usr/bin/python3
"""
Unit tests for the Base class.
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    Define tests for the Base class.
    """

    def test_id_assignment(self):
        """
        Test automatic id assignment.
        """
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base(12)
        self.assertEqual(base3.id, 12)
        base4 = Base()
        self.assertEqual(base4.id, 3)

    def test_json_string(self):
        """
        Test JSON string representation.
        """
        dict1 = {'id': 10, 'width': 7, 'height': 2, 'x': 8, 'y': 3}
        json_str = Base.to_json_string([dict1])
        self.assertTrue(isinstance(json_str, str))


if __name__ == "__main__":
    unittest.main()
