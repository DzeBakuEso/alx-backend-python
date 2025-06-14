#!/usr/bin/env python3
"""
Unittest module for GithubOrgClient
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized_class, parameterized

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'),
                     [TEST_PAYLOAD])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up class: patch requests.get and assign side effects"""
        cls.get_patcher = patch('client.requests.get')
        mock_get = cls.get_patcher.start()

        # Define .json() return values for each call
        mock_get.side_effect = [
            MockResponse(cls.org_payload),
            MockResponse(cls.repos_payload)
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down: stop patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method returns expected repositories"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license filter"""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


class MockResponse:
    """Mocked response object for requests.get().json()"""
    def __init__(self, payload):
        self.payload = payload

    def json(self):
        return self.payload


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @patch('client.get_json')
    def test_org(self, mock_get_json):
        """Test that GithubOrgClient.org returns correct data"""
        payload = {"login": "google", "id": 1}
        mock_get_json.return_value = payload

        client = GithubOrgClient("google")
        self.assertEqual(client.org, payload)
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/google"
        )

    def test_public_repos_url(self):
        """Test the _public_repos_url property"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://test.com/repos"}
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url,
                             "http://test.com/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos returns repo names"""
        mock_get_json.return_value = [
            {"name": "repo1"}, {"name": "repo2"}
        ]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "http://fake-url.com"

            client = GithubOrgClient("google")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2"])
            mock_get_json.assert_called_once_with("http://fake-url.com")
            mock_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license returns correct boolean"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)
