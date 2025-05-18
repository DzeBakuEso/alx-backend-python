import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Unit tests for memoize decorator"""

    def test_memoize(self):
        """Test that a memoized function is only called once"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test_obj = TestClass()

            # Access property twice
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            # Assert values are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Assert method was called only once due to memoization
            mock_method.assert_called_once()
