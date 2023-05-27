# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:49:13 2022

@author: user
"""
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id="my-id", value="Initial Text", type="text"),
    html.Div(id="my-div", style={"border": "2px solid green"})
])


@app.callback(Output(component_id="my-div", component_property="children"),
              [Input(component_id="my-id", component_property="value")])
def update_output_div(value):
    return "You entered {}".format(value)


if __name__ == "__main__":
    app.run()
    
#****************************************************************************
     
#******************************************************************
    
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

df = pd.read_csv(r"C:\Users\user\Desktop\Plotly\Dataset/mpg.csv")

app = dash.Dash()

features = df.columns

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id="xaxis",
                     options=[{
                         "label": i,
                         "value": i
                     } for i in features],
                     value="displacement")
    ],
             style={
                 "width": "48%",
                 "display": "inline-block"
             }),
    html.Div([
        dcc.Dropdown(id="yaxis",
                     options=[{
                         "label": i,
                         "value": i
                     } for i in features],
                     value="mpg")
    ],
             style={
                 "width": "48%",
                 "display": "inline-block"
             }),
    dcc.Graph(id="graph")
],
                      style={"padding": 10})


@app.callback(
    Output("graph", "figure"),
    [Input("xaxis", "value"), Input("yaxis", "value")])
def update_graph(xaxis, yaxis):
    trace = go.Scatter(x=df[xaxis],
                       y=df[yaxis],
                       text=df["name"],
                       mode="markers",
                       marker={
                           "size": 15,
                           "opacity": 0.5,
                           "line": {
                               "width": 0.5,
                               "color": "white"
                           }
                       })

    return {
        "data": [trace],
        "layout":
        go.Layout(title="My Dashboard For MPG",
                  xaxis={"title": xaxis},
                  yaxis={"title": yaxis},
                  hovermode="closest")
    }


if __name__ == "__main__":
    app.run()


#****************************************************************
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
import base64

df = pd.read_csv(r"C:\Users\user\Desktop\Plotly\Dataset/wheels.csv")

app = dash.Dash()


def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, "rb").read())
    return r"C:\Users\user\Desktop\Plotly\Dataset/png;base64,{}".format(encoded.decode())


app.layout = html.Div([
    dcc.RadioItems(id="wheels",
                   options=[{
                       "label": i,
                       "value": i
                   } for i in df["wheels"].unique()],
                   value=1),
    html.Div(id="wheels-output"),
    html.Hr(),
    dcc.RadioItems(id="colors",
                   options=[{
                       "label": i,
                       "value": i
                   } for i in df["color"].unique()],
                   value="blue"),
    html.Div(id="colors-output"),
    html.Img(id="display-image", src="children", height=300),
],
                      style={"fontSize": 18})


@app.callback(Output("wheels-output", "children"), [Input("wheels", "value")])
def callback_wheels(wheels_value):
    return "you choose {}".format(wheels_value)


@app.callback(Output("colors-output", "children"), [Input("colors", "value")])
def callback_colors(color_value):
    return "you choose {}".format(color_value)


@app.callback(Output("display-image", "src"),
              [Input("wheels", "value"),
               Input("colors", "value")])
def callback_image(wheel, color):
    path = r"C:\Users\user\Desktop\Plotly\Dataset/"
    return encode_image(path + df[(df["wheels"] == wheel)
                                  & (df["color"] == color)]["image"].values[0])


if __name__ == "__main__":
    app.run()
    
    
    
#***************************************************
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
app = dash.Dash()

app.layout = html.Div([
    dcc.RangeSlider(id="range",
                    min=-5,
                    max=5,
                    step=1,
                    value=[-2, 2],
                    marks={i: str(i)
                           for i in range(-5, 6)}),
    html.Div(id="ans")
])


@app.callback(Output("ans", "children"), [Input("range", "value")])
def callback_range_slider(value):
    ans = value[0] * value[1]
    return "Multiplication is {}".format(ans)


if __name__ == "__main__":
    app.run()