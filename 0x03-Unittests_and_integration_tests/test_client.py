#!/usr/bin/env python3
"""
Unit tests for the client.GithubOrgClient class.
"""

from unittest import TestCase
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import List


class TestGithubOrgClient(TestCase):
    """
    Test cases for methods in the GithubOrgClient class.
    """

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Mocks the get_json function to avoid making an actual
        API request and tests that the public_repos method returns
        the expected list of repositories from the organization.
        """
        # Define a mock payload that get_json should return
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        # Mock the ret    urn value of get_json
        mock_get_json.return_value = mock_payload

        # Mock the _public_repos_url
        # property to return a specific URL
        url = "client.GithubOrgClient._public_repos_url"
        with patch(url, new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/testorg/repos"

            # Instantiate the client and call the public_repos method
            client = GithubOrgClient("testorg")
            result: List[str] = client.public_repos()

            # Check if the returned list matches the
            # expected list of repo names
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)

            # Verify that _public_repos_url was accessed once
            mock_url.assert_called_once()

            # Verify that get_json was called once
            # with the URL from _public_repos_url
            mock_get_json.assert_called_once_with(
                    "https://api.github.com/orgs/testorg/repos"
                    )


if __name__ == "__main__":
    unittest.main()
