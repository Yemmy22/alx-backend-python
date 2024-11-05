#!/usr/bin/env python3
"""
A TestGithubOrgClient class module
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """
    A unittest subclass
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_org(self, org_name: str, mock_get_json: PropertyMock) -> None:
        """
        Define the return value for the mock
        """
        mock_get_json.return_value = {"name": org_name}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        result: Dict = client.org

        # Test that get_json was called
        # once with the expected argument
        mock_get_json.assert_called_once_with()

        # Test that the returned value is as expected
        self.assertEqual(result, {"name": org_name})
