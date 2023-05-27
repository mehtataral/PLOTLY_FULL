# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:35:01 2022

@author: user
"""
#***************** LINE GRAPH *************************

import numpy as np
import plotly.offline as offline
import plotly.graph_objs as graph

np.random.seed(56)

x_values = np.linspace(0,1,100)
y_values = np.random.random(100)

trace0 = graph.Scatter(
    x=x_values,
    y=y_values + 5,
    mode="markers",
    name="markers"
)

trace1 = graph.Scatter(
    x=x_values,
    y=y_values,
    mode="lines", 
    name="lines"
)

trace2 = graph.Scatter(
    x=x_values,
    y=y_values-5,
    mode="lines+markers", 
    name="lines+markers"
)

data = [trace0, trace1, trace2]

layout = graph.Layout(
    title="Line Chart"
)

fig = graph.Figure(data=data, layout=layout)

offline.plot(fig)

#***************** LINE GRAPH *************************
import pandas as pd
import plotly.offline as offline
import plotly.graph_objs as graph

df = pd.read_csv(r"C:\Users\user\Desktop\Plotly\Dataset/nst-est2017-alldata.csv")
df
df_division_1 = df[df["DIVISION"] == '1']

df_division_1.set_index("NAME", inplace=True)

list_of_pop_col = [
    col for col in df_division_1.columns if col.startswith("POP")
]

df_division_1 = df_division_1[list_of_pop_col]

print(df_division_1.index)
data = [
    graph.Scatter(x=df_division_1.columns,
                  y=df_division_1.loc[name],
                  mode="lines",
                  name=name) for name in df_division_1.index
]

offline.plot(data)

#***************** LINE GRAPH *************************

import pandas as pd
import plotly.graph_objs as graph
import plotly.offline as offline

df = pd.read_csv(r"C:\Users\user\Desktop\Plotly\Dataset/2010YumaAZ.csv")
print(df)
days = [
    "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY",
    "MONDAY"
]

data = []
for day in days:
    day_df = df[df["DAY"] == day]
    trace = graph.Scatter(x=day_df["LST_TIME"],
                          y=day_df["T_HR_AVG"],
                          mode="lines",
                          name=day)
    data.append(trace)

layout = graph.Layout(title="Remperature Data")

fig = graph.Figure(data=data, layout=layout)

offline.plot(fig)
