import requests
from bs4 import BeautifulSoup

# requesting a GET request to the Conversion page to get the list of the most accessed sites in Brazil
url = 'https://www.conversion.com.br/blog/ranking-sites-mais-visitados/'
response = requests.get(url)

# checking if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Table with the most visited websites
    table = soup.find('table')
    data = []
    rows = table.find_all('tr')[1:]

    # Iterate through the rows and collecting the data
    for row in rows:
        cells = row.find_all('td')
        dom = cells[1].text
        access = cells[4].text

        data.append({'Site': dom, 'Acessos': access})

    for item in data:
        print(f"Site: {item['Site']}, Acessos: {item['Acessos']}")

else:
    print('Results not found')
