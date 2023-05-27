# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 12:55:02 2022

@author: user
"""
import pandas as pd
import numpy as np
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


# df = pd.read_csv(r'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')

# df_state_lvl = df.groupby('Province_State').sum()
# df_state_lvl

# df_state_lvl = df.groupby('Province_State', as_index=True).sum()
# df_state_lvl

# df_state_lvl = df.groupby('Province_State', as_index=False).sum()
# df_state_lvl

app =dash.Dash()
app.layout =html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('This is a paragraph.')
    ])
])

if __name__ =="__main__":
    app.run()
    
#*******************************************************

import pandas as pd
import numpy as np
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


app =dash.Dash()
app.layout =html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('This is a paragraph.')
    ]),
    html.Div(
    dcc.Dropdown(id='dropdown', 
    options = [
    {
      'label': 'United States of America',
      'value': 'USA'
    },
    {
      'label': 'India',
      'value': 'IND'
    },
    {
      'label': 'Japan',
      'value': 'JPN'
    }
    ],
  value = 'IND'
))
])

if __name__ =="__main__":
    app.run()
    
#***************************************************************


import pandas as pd
import numpy as np
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px



df = pd.DataFrame({
  "Indicator": ["Total Cases", "Recovered", "Total Cases", "Recovered"],
  "Cases": [19111326, 11219123, 10147468, 9717834],
  "Country": ["USA", "USA", "India", "India"]
})

fig = px.bar(df, x="Indicator", y="Cases", color="Country", barmode="group",color_discrete_map={
        'some_group': 'red',
        'some_other_group': 'green'
    })

app =dash.Dash()
app.layout =html.Div([
    html.H1('Hello Dash',
            style = {
                'textAlign': 'center',
                'color': '#7FDBFF'
                }
            ),
    
    html.Div(
                style = {
                'backgroundColor': '#111111'
                },
                children =[
                   html.P('This is a paragraph.',
                   style = {
                           'textAlign': 'center',
                           'color': '#7FDBFF'
                           }
               )
    ]),
    
    html.Div(
    dcc.Dropdown(id='dropdown', 
    options = [
    {
      'label': 'United States of America',
      'value': 'USA'
    },
    {
      'label': 'India',
      'value': 'IND'
    },
    {
      'label': 'Japan',
      'value': 'JPN'
    }
    ],
  value = 'IND'
)),
    dcc.Graph(
  id = 'example-graph-2',
  figure = fig
)
])
dc =dcc.Dropdown(id='dropdown22', 
options = [
{
  'label': 'United States of America',
  'value': 'USA'
},
{
  'label': 'India',
  'value': 'IND'
},
{
  'label': 'Japan',
  'value': 'JPN'
}
])
if __name__ =="__main__":
    app.run()
    
#***************************************************************
from dash.dependencies import Input, Output
# CALLBACKS
# Callbacks are functions which are called when a particular event occurs.
# Suppose we select a dropdown item, and we want our graph to be updated accordingly. 
# In such cases, we can use callbacks. In Dash we use app.callback decorator for callbacks.
@app.callback(
Output('graph-with-slider', 'figure'),[Input('City-slider', 'value')]           
)

@app.callback(
    Output(component_id='Indicator', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)



def update_figure(selected_month):
    filtered_df = df[df.City == selected_month]

    fig = px.bar(df, x = "Indicator", y = "Cases", hover_name = "Country",log_x = True)

    fig.update_layout(transition_duration = 500)

    return fig




if __name__ =="__main__":
    app.run()































