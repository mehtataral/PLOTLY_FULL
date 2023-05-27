# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:02:23 2022

@author: user
"""
   
##*********************** DROPDOWN + RADIOBUTTON + SLIDER *******************************    
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Label("Dropdown"),
    dcc.Dropdown(options=[{
         "label": "New York City",
         "value": "NYC"
     }, {
        "label": "San Francisco",
        "value": "SF"
    }],
                  value="SF"),
    html.Label("Slider"),
    dcc.Slider(min=-10,
                max=10,
                step=0.5,
                value=0,
                marks={i: "{}".format(i)
                      for i in range(-10, 11)}),
    html.Label("Radio"),
    dcc.RadioItems(options=[{
        "label": "New York City",
        "value": "NYC"
    }, {
        "label": "San Francisco",
        "value": "SF"
    }],
                    value="SF")
])

if __name__ == "__main__":
    app.run()    
    
    
#***************** BAR GRAPH *************************

import plotly.graph_objs as graph
import plotly.offline as offline
import pandas as pd

df = pd.read_csv(r"C:\Users\user\Desktop\Plotly\Dataset/2018WinterOlympics.csv")
df
data = [graph.Bar(x=df["NOC"], y=df["Total"])]

layout = graph.Layout(title="Medals")

fig = graph.Figure(data=data, layout=layout)

offline.plot(fig)

#***************** BAR GRAPH *************************
import plotly.graph_objs as graph
import plotly.offline as offline
import pandas as pd

df = pd.read_csv(r"C:\Users\user\Desktop\Plotly\Dataset/2018WinterOlympics.csv")
trace1 = graph.Bar(x=df["NOC"],
                   y=df["Gold"],
                   name="Gold",
                   marker={"color": "#FFD700"})

trace2 = graph.Bar(x=df["NOC"],
                    y=df["Silver"],
                    name="Silver",
                    marker={"color": "#9EA0A1"})

trace3 = graph.Bar(x=df["NOC"],
                    y=df["Bronze"],
                    name="Bronze",
                    marker={"color": "#CD7F32"})

data = [trace1, trace2, trace3]
# data =trace1
#layout = graph.Layout(title="Medals")
layout = graph.Layout(title="Medals", barmode="stack")

fig = graph.Figure(data=data, layout=layout)

offline.plot(fig)

#***************** BAR GRAPH *************************

import pandas as pd
import plotly.offline as offline
import plotly.graph_objs as graph

df = pd.read_csv(r"C:\Users\user\Desktop\Plotly\Dataset/mocksurvey.csv", index_col=0)
df
data = [
    graph.Bar(x=df[col], y=df.index, orientation="h", name="Question 1")
    for col in df.columns
]

layout = graph.Layout(title="Survey", barmode="stack")

fig = graph.Figure(data=data, layout=layout)

offline.plot(fig)

