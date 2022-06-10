
import numpy as np
from dash import dcc
from dash import html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

from plotly.subplots import make_subplots

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Piechart', external_stylesheets=external_stylesheets)
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

df['RSP/L'] = df['RSP/L'].replace(0, np.nan)

from sklearn.impute import SimpleImputer

imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imp = imp.fit_transform(df)

df = pd.DataFrame(imp, columns=df.columns)


df = df[df['RSP/L'] > 27.555]


companies = df['Company'].value_counts()
labels = companies.keys()


app.layout = html.Div([
    html.H4('Companies'),
    dcc.Graph(id='line-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    html.Div(
        id='line-updatemode',
        
    ),
])


@app.callback(
               Output('line-graph', 'figure'),
              [Input('line-updatemode', 'value')])
def display_value(value):
         
    
    
    graph = go.Pie(labels=labels, values=companies, scalegroup='one',
                        name="Fuel Company")    
    
    layout = go.Layout(
        title='Showing the Regions',
        paper_bgcolor='#27293d',
        font=dict(color='white'),
        showlegend=True

    )
    
    

    return {'data': [graph], 'layout': [layout]}



