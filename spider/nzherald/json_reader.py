import json
import requests
from bs4 import BeautifulSoup

# Open a text file and write the titles
output = open('nzherald_articles_Christchurch_shooting.md', 'w', encoding='utf-8')

# Path to your JSON file
filename = 'nzherald_shooting.json'

# Open the JSON file for reading
with open(filename, 'r') as file:
    # Load JSON data from file
    data = json.load(file)

# Access data (Object)
# print(data) 

#  h1 dcr-h5yuj3
#  div dcr-1qp23oo
#  <div id="maincontent" class="dcr-lw02qf">
#  p dcr-4cudl2
#
# iterate links in the object 
for item in data:
    # URL of the webpage you want to scrape
    url = item['link']
    # Send a GET request to the webpage
    response = requests.get(url)
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # title 
    try:
        h1_title = soup.find('h1', {'class':'article__heading'})
        output.write('## ' + str(item['position']) + ', ' + h1_title.get_text() + '\n\n')
    except: 
        output.write('## ' + str(item['position']) + ' None\n\n')
    # link
    output.write(item['link'] + '\n\n')
    # paragraphs 
    try:
        body = soup.find('section', {'class': 'article__body'})
        paragraphs = body.find_all('p')
        for p in paragraphs:
            output.write(p.text + '\n\n')
    except: 
         output.write('None\n\n')
    print(item["position"], item["title"])

output.close()

