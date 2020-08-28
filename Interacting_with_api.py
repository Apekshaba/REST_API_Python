#importing all the neccessary modules for the script
import requests
import csv

# requesting data from the API
result = requests.get(input("Enter API url from where you want to fetch data:"))
if result.status_code >= 200:   
    result = result.json()
else:
    raise ValueError

new_result = result['items']

#filtering out only 5 columns from the data 
filtered_data = {}
def filter_func():
    for data in new_result:
        filtered_data = {column: data[column] for column in ("name", "description", "html_url", "stargazers_count", "watchers_count")}
    return filtered_data


#writting filtered data into the csv file 
def write_in_csv():
    data_after_filteration = filter_func()
    field_names = data_after_filteration.keys()

    with open('data.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        for data in data_after_filteration:
            writer.writerow(data)
          
      return {"message":"Successfully written!"}


if __name__ == "__main__":
    write_in_csv()
