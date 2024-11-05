#!/usr/bin/env python3
"""
A TestAccessNestedMap class module
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    """
    A unittest subclass
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Configure the mock to return a response with
        a json method that returns test_payload
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function being tested
        result = get_json(test_url)

        # Assert that the mock was called once with the expected URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the result matches the expected payload
        self.assertEqual(result, test_payload)
