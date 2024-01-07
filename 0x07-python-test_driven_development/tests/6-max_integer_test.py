#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the max_integer function."""

    def test_positive_integers(self):
        """Test with all positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        """Test with all negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test with a mix of positive and negative integers."""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_single_element(self):
        """Test with a single element in the list."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_repeated_elements(self):
        """Test with repeated elements in the list."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_non_integers(self):
        """Test with non-integer elements in the list (should fail)."""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3.5])


if __name__ == '__main__':
    unittest.main()
