import requests
from bs4 import BeautifulSoup

# basic request
# response = requests.get("https://oxylabs.io/")
# print(response.text)

# with form
# form_data = {'key1': 'value1', 'key2': 'value2'}
# response = requests.post('https://httpbin.org/post', data=form_data)
# print(response.text)

# getting pokemon
url = "https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser') 
print(soup.title)