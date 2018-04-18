
# coding: utf-8

# In[9]:


import pandas as pd

# Import and clean the data
df = pd.read_csv('data.csv',converters={'price': lambda s: (s.replace('$', ''))})

df = df[['name', 'latitude', 'longitude', 'price']]
df.price = df.price.str.replace(',','')
df.price = pd.to_numeric(df.price)


# In[10]:


# Set all the credentials
import plotly

plotly.tools.set_credentials_file(username='', api_key='')

import plotly.plotly as py
from plotly.graph_objs import *

mapbox_access_token = ''


# In[7]:


# Filter results for anomalies with listings of thousands of euros per night
df = df[df.price < 200]


# In[8]:


# Plot the graph
data = Data([

    Scattermapbox(
        lat=df.latitude,
        lon=df.longitude,
        mode='markers',
        #text=df.name,
        marker=Marker(
            size=8,
            color=df.price,
            colorbar=ColorBar(
                title='Price'
            ),
            opacity=0.7
        ),
        hoverinfo='none'
    )]
)
        
layout = Layout(
    title='AirBnB Madrid',
    autosize=True,
    hovermode='closest',
    showlegend=False,
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=40.5,
            lon=-3.5
        ),
        pitch=0,
        zoom=7,
        style='light'
    ),
)

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='AirBnb Madrid')

