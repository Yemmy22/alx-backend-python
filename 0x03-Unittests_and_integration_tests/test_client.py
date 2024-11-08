#!/usr/bin/env python3
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from typing import Dict, Any, List

# Example structure for TEST_PAYLOAD if you haven't already defined it.
# Ensure that each fixture is defined as expected.
TEST_PAYLOAD = [
    (
        {"login": "google"},  # org_payload
        [{"name": "repo1"}, {"name": "repo2"}],  # repos_payload
        ["repo1", "repo2"],  # expected_repos
        ["repo1"]  # apache2_repos
    ),
    # You can add more payload tuples as needed
]

@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(TestCase):
    """Integration tests for the GithubOrgClient public_repos method."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up the class by patching requests.get."""
        cls.get_patcher = patch("requests.get")

        # Start the patcher
        cls.mock_get = cls.get_patcher.start()

        # Define side effects based on expected URLs
        def side_effect(url: str):
            if "orgs" in url:
                return cls.org_payload
            elif "repos" in url:
                return cls.repos_payload
            return {}

        # Set the side effect for the mock
        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Test the public_repos method."""
        client = GithubOrgClient("google")
        result = client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_apache2_repos(self) -> None:
        """Test filtering for Apache 2 licensed repos."""
        client = GithubOrgClient("google")
        result = [repo for repo in client.public_repos() if client.has_license(repo, "apache-2.0")]
        self.assertEqual(result, self.apache2_repos)
