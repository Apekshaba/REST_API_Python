#importing all the neccessary modules for the script
import requests
import csv


result = requests.get(input("Enter API url from where you want to fetch data:"))
if result.status_code >= 200:
    result = result.json()
else:
    raise ValueError

new_result = result['items']

filtered_data = {}
def filter_func():
    for data in new_result:
        filtered_data = {column: data[column] for column in ("name", "description", "html_url", "stargazers_count", "watchers_count")}
    return filtered_data


def write_in_csv():
    data_after_filteration = filter_func()
    field_names = data_after_filteration.keys()

    with open('data.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data_after_filteration)

write_in_csv()
