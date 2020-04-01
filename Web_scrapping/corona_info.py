#https://regex101.com/

import re
import requests

def get_number_of_infected():
    page = requests.get('https://www.worldometers.info/coronavirus/country/poland/')
    # f = open('data_nowa.txt', 'w')
    # f.write(page.text)

    pattern = r'Poland Coronavirus: (\d,{0,1}\d{0,})'
    obj = re.search(pattern, page.text)
    return obj.group(1)


file = '/Users/Bury/Applications/github/Python_projects/Web_scrapping/data.txt'

with open(file, 'r') as f:
    saved_datad = f.readline()
    print(saved_datad)

current_data = get_number_of_infected()

if saved_datad != current_data: 
    with open(file, 'w') as f:
        f.write(str(current_data))
    print(f"update data: {current_data} people infected")
else:
    print("nothing to upadate")