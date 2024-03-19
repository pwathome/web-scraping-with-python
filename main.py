# imports
import requests
from bs4 import BeautifulSoup

# url endpoint
url = 'https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon'
# respose from request 
response = requests.get(url)
# making soup with response text
soup = BeautifulSoup(response.text, 'html.parser') 
# find first table using attribute and class name
table = soup.find('table', class_='wikitable')
# initialize empty header and row tuple
header = []
rows = []

# loop through table rows
for i, row in enumerate(table.find_all('tr')):
    # if first row, set header
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    # otherwise append each row to the rows tuple
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

for row in rows:
    print(row)


# ['#', 'Sprite', 'Name', 'Type 1', 'Type 2', 'Japanese', 'Official rom.']
print(header)
