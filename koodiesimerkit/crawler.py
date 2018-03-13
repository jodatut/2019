import requests
import pandas as pd

from bs4 import BeautifulSoup

response = requests.get('https://www.finnkino.fi/elokuvat/ohjelmistossa')

# print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

# Convert to string
pretty = soup.prettify()
# print(pretty)

# Write to external file
with open("output1.html", "w") as file:
    file.write(pretty)
    
movies = soup.select('h2 a')    # Soup object type
titles = []
links = []

# Go through all movies in catalog
for movie in movies:
    
    # Get movie title and movie URL
    title = movie.text
    titles.append(title)
    links.append(movie.get('href'))
   
directors = []

# Go through all movie URLs and get director
for link in links:
    
    response = requests.get(link)
    
    soup = BeautifulSoup(response.content, 'html.parser') 
    
    # Director is the first in a elements
    a_elements = soup.select('span a')
    directors.append(a_elements[0].text)
 
# Adding movies to pandas dataframe
df = pd.DataFrame({'Movie':titles, 'Director':directors})

df.to_csv('movies.csv', encoding='utf8')
