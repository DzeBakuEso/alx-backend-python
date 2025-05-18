import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    # ... other tests

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Unit-test GithubOrgClient.public_repos method"""

        # Arrange: set up mocked get_json to return a list of repo dicts
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        test_url = "https://api.github.com/orgs/testorg/repos"
        client = GithubOrgClient("testorg")

        with patch.object(GithubOrgClient, "_public_repos_url", new_callable=PropertyMock) as mock_public_repos_url:
            # Mock _public_repos_url to return the test URL
            mock_public_repos_url.return_value = test_url

            # Act: call public_repos
            repos = client.public_repos()

            # Assert: public_repos returns the repo names from mocked get_json
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])

            # Assert: _public_repos_url property was accessed once
            mock_public_repos_url.assert_called_once()

            # Assert: get_json was called once with the mocked URL
            mock_get_json.assert_called_once_with(test_url)
