#!/usr/bin/env python3
"""Unittests for GithubOrgClient._public_repos_url (Task 5)."""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit test class for GithubOrgClient methods."""

    def test_public_repos_url(self):
        """
        Test that _public_repos_url returns the expected repos_url
        from the mocked org payload.
        """
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}

        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, payload["repos_url"])
