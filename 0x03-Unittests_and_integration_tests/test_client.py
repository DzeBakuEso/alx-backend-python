import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized_class
import requests

from client import GithubOrgClient  # Adjust if your import path differs
import fixtures  # Make sure fixtures.py is in the same directory


@parameterized_class([
    {
        "org_payload": fixtures.org_payload,
        "repos_payload": fixtures.repos_payload,
        "expected_repos": fixtures.expected_repos,
        "apache2_repos": fixtures.apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Patch requests.get globally for all tests in this class
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define side_effect function to return different payloads based on URL
        def side_effect(url, *args, **kwargs):
            mock_resp = MagicMock()
            if url == cls.org_payload['repos_url']:
                mock_resp.json.return_value = cls.repos_payload
            elif url == f"https://api.github.com/orgs/{cls.org_payload['login']}":
                mock_resp.json.return_value = cls.org_payload
            else:
                mock_resp.json.return_value = {}
            return mock_resp

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        # Initialize GithubOrgClient with the org login from the fixture
        client = GithubOrgClient(self.org_payload['login'])
        repos = client.public_repos()

        # Test if returned repos match the expected repos list
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        client = GithubOrgClient(self.org_payload['login'])
        repos_with_apache2 = client.public_repos(license="apache-2.0")
        self.assertEqual(repos_with_apache2, self.apache2_repos)
