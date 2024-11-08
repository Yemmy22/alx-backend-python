#!/usr/bin/env python3
"""
Unit tests for the client.GithubOrgClient class.
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for methods in the GithubOrgClient class.
    """

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),  # Edge case: repo has no license key
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that has_license returns the expected result for
        different repos and license keys.
        """
        client = GithubOrgClient("testorg")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
