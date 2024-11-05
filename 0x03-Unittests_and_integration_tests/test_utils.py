#!/usr/bin/env python3
"""
A TestAccessNestedMap class module
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    A unittest subclass
    """
    @parameterized.expand([
        ({}, ("a",)),  # Empty nested map, path has "a"
        ({"a": 1}, ("a", "b"))  # Nested map has "a"
        # key, path includes "b" which doesn't exist
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that the method raises the correct exception
        """
        # Check if KeyError is raised with the expected message
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        # Verify the exception message matches the missing key
        self.assertEqual(str(context.exception), "'" + path[-1] + "'")


if __name__ == '__main__':
    unittest.main()
