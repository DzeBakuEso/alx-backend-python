#!/usr/bin/env python3
"""
Unit tests for the client module.
"""

import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized

from client import (
    GithubOrgClient
)
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mock_get_json: MagicMock) -> None:
        """
        Test that GithubOrgClient.org returns correct value.
        """
        test_payload = {"login": org}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org)
        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )

    def test_public_repos_url(self) -> None:
        """
        Test that _public_repos_url returns expected URL.
        """
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/testorg/repos"
            }
            client = GithubOrgClient("testorg")
            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/testorg/repos"
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """
        Test that public_repos returns the list of repository names.
        """
        payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = payload

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/testorg/repos"
            client = GithubOrgClient("testorg")
            self.assertEqual(
                client.public_repos(),
                ["repo1", "repo2", "repo3"]
            )
            mock_get_json.assert_called_once()
            mock_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other"}}, "my_license", False)
    ])
    def test_has_license(
        self,
        repo: dict,
        license_key: str,
        expected: bool
    ) -> None:
        """
        Test that has_license returns the correct boolean.
        """
        client = GithubOrgClient("testorg")
        self.assertEqual(client.has_license(repo, license_key), expected)


if __name__ == '__main__':
    unittest.main()
