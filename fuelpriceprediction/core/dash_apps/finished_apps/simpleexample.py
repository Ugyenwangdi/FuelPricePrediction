from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.H4('Welcome '),
    html.Div([
        
        html.Div([
            html.P("This dashboard displays an Analysis of Bhutans' Fuel Price Data through visualization. "),
            dcc.Markdown('''
##### Guidelines: 
1. Use the **side navigation bar** to view different analysis of fuel data.
2. Use the **Home** button on the top right corner to predict the fuel price.
Markdown is a simple way to write and format text.

''')
        ])
    ])
    
    


    
])


@app.callback(
               Output('slider-graph', 'figure'),
              [Input('slider-updatemode', 'value')])
def display_value(value):


    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),

    )
    
    # return {'layout': layout}