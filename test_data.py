import unittest
from Interacting_with_api import csv_generator
import pandas as pd
import requests

result = requests.get("https://api.github.com/search/repositories?q=is:public").json()
data = pd.read_csv("data.csv",usecols=['name', 'description', 'html_url', 'watchers_count', 'stargazers_count', 'forks_count'])


class test_data_output(unittest.TestCase):
    def test_write_in(self):
        self.assertAlmostEqual(csv_generator.write_in(result), data)

if __name__ == '__main__':
    test_data_output().test_write_in()
