#!/usr/bin/env python3
"""
Unit tests for the client.GithubOrgClient class.
"""

from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for GithubOrgClient class methods.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', new_callable=PropertyMock)
    def test_org(self, org_name: str, mock_get_json: PropertyMock) -> None:
        """
        Test that GithubOrgClient.org returns the
        correct value and that get_json is called
        once with the expected argument.
        """
        mock_get_json.return_value = {"name": org_name}

        client = GithubOrgClient(org_name)
        result: Dict = client.org

        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
                )
        self.assertEqual(result, {"name": org_name})
