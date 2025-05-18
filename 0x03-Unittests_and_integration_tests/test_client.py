import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    # ... (previous tests)

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url returns the correct URL from org payload"""
        with patch.object(GithubOrgClient, "org", new_callable=unittest.mock.PropertyMock) as mock_org:
            # Arrange: mock org property to return a specific payload
            mock_org.return_value = {"repos_url": "https://api.github.com/orgs/testorg/repos"}

            # Act
            client = GithubOrgClient("testorg")
            result = client._public_repos_url

            # Assert
            self.assertEqual(result, "https://api.github.com/orgs/testorg/repos")
