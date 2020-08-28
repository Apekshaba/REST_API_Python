import unittest
from interacting_with_api import filter_func,filtered_data

class TestData(unittest.TestCase):
    def test_filter_func(self):
        actual = filter_func()
        self.assertEqual(actual,filtered_data)

if __name__ == '__main__':
    unittest.main()
