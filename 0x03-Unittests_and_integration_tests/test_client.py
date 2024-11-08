#!/usr/bin/env python3
"""
Unit tests for the client.GithubOrgClient class.
"""

from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for GithubOrgClient class methods.
    """

    def test_public_repos_url(self):
        """
        Test that _public_repos_url returns
        the correct URL based on the org's data.
        """
        mock_payload = {
                "repos_url": "https://api.github.com/orgs/google/repos"
                }

        # Patch the `org` property with a
        # PropertyMock to return the dictionary directly
        with patch(
                'client.GithubOrgClient.org', new_callable=PropertyMock
                ) as mock_org:
            mock_org.return_value = mock_payload

            client = GithubOrgClient("google")

            # Access the _public_repos_url property
            result = client._public_repos_url

            # Verify that _public_repos_url gives the expected repos_url
            self.assertEqual(result, mock_payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
