#importing all the neccessary modules for the script
import pandas as pd
import requests
import csv
from abc import ABC, abstractmethod
import os

# environment variable
APP_ID = os.getenv("APP_USER")

# fetching the data from given public api and also checking for the possible errors it could throw
result = requests.get("https://api.github.com/search/repositories?q=is:public").json()  #converting it to the json format
if not result:
    raise ValueError
else:
    pass

#creating an abstract class for writing data into a seperate format
class data_generator(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()


    @abstractmethod
    def write_in(result):
        pass


#class to generate csv file which is inheriting data_generator class
class csv_generator(data_generator):

    def append_data(result):
        with open("data.csv",'r') as csvdata:
            comp1 = list(csvdata.readline(result,limit=1))
            writer = csv.DictWriter(csvdata)
            if(comp1 == list(writer.writeheader())):
                writer.writerows(result["items"])
            else:
                writer.writeheader()  # writting headers to the csv file
                writer.writerows(result["items"])


    def write_in(result):#abstract method of csv_generator class
        try:
            field_names = result["items"][0].keys() #fetching all the field names from the data being fetched

            with open('data.csv', 'a'):
                result.append_data(result)
            #fetching the only columns we want from the csv file we generated
            data=pd.read_csv("data.csv",usecols=['name','description','html_url','watchers_count','stargazers_count','forks_count'])
        except Exception:
            raise ValueError
            return data


class xls_generator(data_generator):

    def write_in(self):
        pass