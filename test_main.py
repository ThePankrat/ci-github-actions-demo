# test_main.py
import unittest
from main import add

class TestMain(unittest.TestCase):

    def test_add(self):
        """Test the add function with positive numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 5), 15)

    def test_add_negative(self):
        """Test the add function with negative numbers."""
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()