import requests
import pandas as pd

from bs4 import BeautifulSoup

response = requests.get('https://www.finnkino.fi/elokuvat/ohjelmistossa')

# print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

# Convert to string
pretty = soup.prettify()
# print(pretty)

with open("output1.html", "w") as file:
    file.write(pretty)
    
movies = soup.select('h2 a')    # Soup object type
titles = []

for movie in movies:
    
    title = movie.text
    titles.append(title)
    
# Adding movies to pandas dataframe
df = pd.DataFrame({'Movie':titles})

df.to_csv('movies.csv', encoding='utf8')