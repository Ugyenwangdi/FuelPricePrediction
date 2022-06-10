import numpy as np
from dash import dcc
from dash import html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Linechart', external_stylesheets=external_stylesheets)
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
# print(df.head())


df = df[df['RSP/L'] > 27.555]

petroldf = df[df['Product']=='Petrol']
dieseldf = df[df['Product']=='Diesel']

petrolg = petroldf[petroldf['Station']=='Gyelposing']
dieselg = dieseldf[dieseldf['Station']=='Gyelposing']



p = petrolg.sort_values(by='Approved_Date')
d = dieselg.sort_values(by='Approved_Date')

# print(df.isnull().sum())


app.layout = html.Div([
    html.H4('Change of Fuel Prices'),
    dcc.Graph(id='line-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    html.Div(
        id='line-updatemode',
        
    ),
])


@app.callback(
               Output('line-graph', 'figure'),
              [Input('line-updatemode', 'value')])
def display_value(value):
    
    graph = go.Scatter(x = p['Approved_Date'], y = p['RSP/L'],
                  name='Petrol Price per L (in NU)')
    
    graph2 = go.Scatter(x = d['Approved_Date'], y = d['RSP/L'],
                  name='Diesel Price per L (in NU)')

    layout = go.Layout(
        title='Fuel Prices of Gyelpozhing over time (2020-01-15 - 2022-04-01)',
        paper_bgcolor='#27293d',
        font=dict(color='white'),
        showlegend=True

    )

    return {'data': [graph, graph2], 'layout': layout}



