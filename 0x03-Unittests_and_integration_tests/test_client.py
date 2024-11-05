#!/usr/bin/env python3
"""
A TestGithubOrgClient class module
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    A unittest subclass
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')  # Mock get_json in the client module
    def test_org(self, org_name, mock_get_json):
        """
        Define the return value for the mock
        """
        mock_get_json.return_value = {"name": org_name}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Test that get_json was called
        # once with the expected argument
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
                )

        # Test that the returned value is as expected
        self.assertEqual(result, {"name": org_name})
