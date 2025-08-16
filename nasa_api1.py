'''
Script description: 
Get and read data from nasa API about space 
Nasa API: https://api.nasa.gov/
Dev: Sofia Ch.
https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={API_KEY_HERE}
'''

import os 
import requests

os.system('clear')
def get_nasa_data(api_key):
    print("::: NASA INFORMATION:::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try: 
        #API request 
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")    

NASA_API_KEY = "cqPwMqZhBpj7JZ4zmbHtuMApSi7aEdiyt4QMJEzS"
get_nasa_data(NASA_API_KEY)

