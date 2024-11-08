#!/usr/bin/env pthon3
"""
A module for testing the client module.
"""

import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for GithubOrgClient class methods.
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(
            self, org: str,
            expected_response: Dict,
            mocked_get_json: MagicMock
            ) -> None:
        """
        Test the org method of GithubOrgClient
        """
        mocked_get_json.return_value = expected_response
        goclient = GithubOrgClient(org)
        self.assertEqual(goclient.org, expected_response)
        mocked_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org}"
                )

    def test_public_repos_url(self) -> None:
        """
        Test the _public_repos_url property of GithubOrgClient.
        """
        with patch(
                "client.GithubOrgClient.org", new_callable=PropertyMock
                ) as mock_org:
            mock_org.return_value = {
                    'repos_url': "https://api.github.com/users/google/repos"
                    }
            self.assertEqual(
                    GithubOrgClient("google")._public_repos_url,
                    "https://api.github.com/users/google/repos"
                    )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """
        Test the public_repos method of GithubOrgClient.
        """
        test_payload = [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = test_payload
        url = "client.GithubOrgClient._public_repos_url"
        with patch(
                url, new_callable=PropertyMock
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value =\
                    "https://api.github.com/users/google/repos"
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "apache-2.0"}}, "apache-2.0", True),
        ({"license": {"key": "mit"}}, "apache-2.0", False),
    ])
    def test_has_license(
            self, repo: Dict, license_key: str, expected: bool
            ) -> None:
        """Test the has_license method of GithubOrgClient."""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient with fixtures and mocks."""

    @classmethod
    def setUpClass(cls) -> None:
        """
        Setup the class with mock requests to simulate
        GitHub API responses.
        """
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{"json.return_value": route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """
        Test public_repos returns the expected repository names.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """
        Test public_repos filters repositories by the given license.
        """
        client = GithubOrgClient("google")
        self.assertEqual(
                client.public_repos(license="apache-2.0"),
                self.apache2_repos
                )

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Stop the patcher after all tests.
        """
        cls.get_patcher.stop()
