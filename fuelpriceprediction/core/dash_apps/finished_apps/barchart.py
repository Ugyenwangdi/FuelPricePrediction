import numpy as np
import pandas as pd
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Barchart', external_stylesheets=external_stylesheets)

df = pd.read_csv('bhutan_fuel_prices.csv') 
# print(df.head())
# print('hello')

df['Product'] = df['Product'].replace('HSD (in KL)', 'Diesel')
df['Product'] = df['Product'].replace('MS (in KL)', 'Petrol')


index_names = df[ df['Region'] == '\x1a' ].index
  
# drop these row indices from dataFrame
df.drop(index_names, inplace = True)

# Drop the "RSP/KL" column
df.drop(["RSP/KL"], axis = 1, inplace = True)

from sklearn.impute import SimpleImputer

imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imp = imp.fit_transform(df)

df = pd.DataFrame(imp, columns=df.columns)

x = df.Region.unique()
y = df.Region.value_counts()

stations = df.Station.unique()
stationsc = df.Station.value_counts()
app.layout = html.Div([
    html.H4('Number of price changes in different Stations'),
    dcc.Graph(id='bar-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff', 'margin-bottom':'8px'}),
    html.Div(
        id='bar-updatemode',
        
    ),
    html.Br(),
    
])


@app.callback(
               Output('bar-graph', 'figure'),
              [Input('bar-updatemode', 'value')])
def display_value(value):
    
    graph = go.Bar(x=stations, y=stationsc)


    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        margin=dict(t=50, b=225), # Where l r t b correspond to left, right, top, bottom

    )
    
     
    return {'data': [graph], 'layout': layout}