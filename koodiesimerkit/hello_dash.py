import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()

# Data from http://data.insideairbnb.com/spain/comunidad-de-madrid/madrid/2018-01-17/data/listings.csv.gz
df = pd.read_csv('data.csv')
df = df[['bedrooms', 'price', 'name', ]]

app.layout = html.Div([
    html.H1('AirBnb Madrid, Prices per bedrooms'),
    dcc.Graph(
        id='airbnb',
        figure={
            'data': [
                go.Scatter(
                    x=df['price'],
                    y=df['bedrooms'],
                    mode='markers',
                    opacity='0.7',
                    marker={
                        'size':15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                )
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Prices'},
                yaxis={'title': 'Bedrooms'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()
