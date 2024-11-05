#!/usr/bin/env python3
"""
A TestAccessNestedMap class module
"""

import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """
    A unittest subclass
    """
    def test_memoize(self):
        """
        Define the class with a method and a memoized property
        """
        class TestClass:
            """
            Creates test object
            """
            def a_method(self):
                """
                Returns an integer
                """
                return 42

            @memoize
            def a_property(self):
                """
                Returns the return value of the test objects property
                """
                return self.a_method()

        # Create an instance of TestClass
        test_instance = TestClass()

        # Patch the a_method to be a mock
        with patch.object(
                TestClass, 'a_method', return_value=42
                ) as mock_method:
            # Call the memoized property twice
            result_first_call = test_instance.a_property
            result_second_call = test_instance.a_property

            # Assert that the result is as expected
            self.assertEqual(result_first_call, 42)
            self.assertEqual(result_second_call, 42)

            # Assert that a_method was called only once
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
