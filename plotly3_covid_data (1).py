# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 12:55:02 2022

@author: user
"""
# First know and understand your requirements for dashboard.
# Start app with simple layout and callbacks.
# Add dash components and callbacks one by one.
# Refresh app page on local host after addition or deletion to see changes.
# Write separate codes for app, index, data, users etc to make it easy to debug and understand.
# Experiment with different style and app layout for better appearance.
# Share data between callbacks and use multiple outputs callbacks.
# Test app on your local before deployment.
# Deploy a simple app first and then scale.

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

# fig = px.bar(df, x="Indicator", y="Cases", color="Country", barmode="group",color_discrete_map={
#         'some_group': 'red',
#         'some_other_group': 'green'
#     })

# fig = px.bar(df, x="Indicator", y="Cases", color="Country", barmode="group")
fig = px.bar(df, x="Indicator", y="Cases", barmode="group",color="Country",
             color_discrete_map={'USA':'green',
                                 'India':'pink',
                                 })

app =dash.Dash()
app.layout =html.Div(
    children =[
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
  figure = fig,
  
)
])
# dc =dcc.Dropdown(id='dropdown22', 
# options = [
# {
#   'label': 'United States of America',
#   'value': 'USA'
# },
# {
#   'label': 'India',
#   'value': 'IND'
# },
# {
#   'label': 'Japan',
#   'value': 'JPN'
# }
# ])
if __name__ =="__main__":
    app.run()
    
#***************************************************************
# from dash.dependencies import Input, Output
# # CALLBACKS
# # Callbacks are functions which are called when a particular event occurs.
# # Suppose we select a dropdown item, and we want our graph to be updated accordingly. 
# # In such cases, we can use callbacks. In Dash we use app.callback decorator for callbacks.
# @app.callback(
# Output('graph-with-slider', 'figure'),[Input('City-slider', 'value')]           
# )

# @app.callback(
#     Output(component_id='Indicator', component_property='figure'),
#     Input(component_id=geo_dropdown, component_property='value')
# )



# def update_figure(selected_month):
#     filtered_df = df[df.City == selected_month]

#     fig = px.bar(df, x = "Indicator", y = "Cases", hover_name = "Country",log_x = True)

#     fig.update_layout(transition_duration = 500)

#     return fig




# if __name__ =="__main__":
#     app.run()

#***********************************************************************

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

# fig = px.bar(df, x="Indicator", y="Cases", color="Country", barmode="group",color_discrete_map={
#         'some_group': 'red',
#         'some_other_group': 'green'
#     })

# fig = px.bar(df, x="Indicator", y="Cases", color="Country", barmode="group")
fig = px.bar(df, x="Indicator", y="Cases", barmode="group",color="Country",
             # color_discrete_map={'USA':'green',
             #                     'India':'pink',
             #                     })
             color_discrete_sequence=["orange", "red"]
             )
fig.update_layout(showlegend=True)
fig.update_layout(legend = dict(bgcolor = 'yellow'))
fig.update_layout({
'plot_bgcolor': 'rgba(110, 30, 20, 80)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})
app =dash.Dash()
app.layout =html.Div(
    style = {
            'backgroundColor': '#111111'
            },
    children =[
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
  figure = fig,
  
)
])

if __name__ =="__main__":
    app.run()



#***********************************************************************

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

# fig = px.bar(df, x="Indicator", y="Cases", color="Country", barmode="group",color_discrete_map={
#         'some_group': 'red',
#         'some_other_group': 'green'
#     })

# fig = px.bar(df, x="Indicator", y="Cases", color="Country", barmode="group")
fig = px.bar(df, x="Indicator", y="Cases", barmode="group",color="Country",
             # color_discrete_map={'USA':'green',
             #                     'India':'pink',
             #                     })
             color_discrete_sequence=["orange", "red"],template="plotly_dark"
             )
fig.update_layout(showlegend=True)
fig.update_layout(legend = dict(bgcolor = 'black'))
fig.update_layout({
'plot_bgcolor': 'rgba(110, 30, 20, 80)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})
app =dash.Dash()
app.layout =html.Div(
    style = {
            'backgroundColor': '#111111'
            },
    children =[
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
       # config={'displayModeBar': True},
  id = 'example-graph-2',
  figure = fig,
  
)
])

if __name__ =="__main__":
    app.run()



from dash.dependencies import Input, Output



# Input() and Output() take the id of a component 
# (e.g. in dcc.Graph(id='timeseries') the components id is 'timeseries') and 
# the property of a component as arguments.

@app.callback(
    Output(component_id='example-graph-2', component_property='figure'),
    [Input(component_id='dropdown', component_property='value')]
)
def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run()

#***************************************************************************

from dash import Dash, dcc, html, Input, Output

app = dash.Dash()

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run()
#***************************************************************************

f = pd.DataFrame({
  'student_id' : range(1, 11),
  'score' : [1, 5, 2, 5, 2, 3, 1, 5, 1, 5]
})
app = dash.Dash()

app.layout = html.Div([
 	dcc.Dropdown(list(range(1, 6)), 1, id='score'),
 	'was scored by this many students:',
 	html.Div(id='output'),
])

@app.callback(Output('output', 'children'), Input('score', 'value'))
def update_output(value):
 	global df
 	df = df[df['score'] == value]
 	return len(df)


if __name__ == '__main__':
    app.run()
    
#***************************************************************************

import dash 
import pandas as pd
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

df = pd.DataFrame({
  "Indicator": ["Total Cases", "Recovered", "Total Cases", "Recovered"],
  "Cases": [19111326, 11219123, 10147468, 9717834],
  "Country": ["USA", "USA", "India", "India"]
})

# fig = px.bar(df, x="Indicator", y="Cases", color="Country", barmode="group",color_discrete_map={
#         'some_group': 'red',
#         'some_other_group': 'green'
#     })

# fig = px.bar(df, x="Indicator", y="Cases", color="Country", barmode="group")
fig = px.bar(df, x="Indicator", y="Cases", barmode="group",color="Country",
             # color_discrete_map={'USA':'green',
             #                     'India':'pink',
             #                     })
             color_discrete_sequence=["orange", "red"],template="plotly_dark"#,width =12
             )
fig.update_layout(showlegend=True)
fig.update_layout(legend = dict(bgcolor = 'black'))
fig.update_layout({
'plot_bgcolor': 'rgba(110, 30, 20, 80)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})
app =dash.Dash()

app.layout = html.Div(
    style ={
    "backgroundColor":"#111111",
    "textAlign":"Center",
    },children =[
    
    html.Div(
            "Hello",
            style ={
                "color":"white",
                "backgroundColor":"#000021",
                "textAlign":"Center",
                },
        ),
    html.H1("I'm Taral Mehta",
            style ={
                "color":"white",
                "backgroundColor":"#78865",
                "textAlign":"Center",
                }),

    dcc.Dropdown(id ="dropdown",
                 style ={
                     "backgroundColor":"Pink",
                     "textAlign":"Center",
                     "color":"Gold"
                     },
        options = [
            {
                'label':"Excellent",
                'value':100
            },
            {
                "label":"Good",
                'value':70
            },
            {
                'label':"Ok",
                'value':40
            }
            ],
            value = 70,
       ),
    html.Br(),
    dcc.Graph(
        id ="graph1",
         figure= fig,
        ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(id="output_file",
             style ={
                 "backgroundColor":"Yellow",
                 "textAlign":"Center",
                 "color":"Red",
                 "fontSize":20
                 }
             )
    
    ]
 )

@app.callback(
     Output(component_id ="output_file",component_property="children"),
    [Input(component_id ="dropdown",component_property="value")]
    )
def basic_callback(input_value):
    return input_value

if __name__ == '__main__':
    app.run()
        

#***************************************************************************

import dash 
import pandas as pd
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
df = pd.DataFrame({
  "Indicator": ["Total Cases", "Recovered", "Total Cases", "Recovered","Total Cases", "Recovered"],
  "Cases": [29111326, 11219123, 15147468, 9717834,8178340,971780],
  "Country": ["USA", "USA", "India", "India","Russia","Russia"],
  "Year":[2020,2021,2020,2021,2020,2022]
})
pd.options.plotting.backend ="plotly"
pd.options.plotting.backend ="matplotlib"
# fig = px.bar(df, x="Indicator", y="Cases", color="Country", barmode="group",color_discrete_map={
#         'some_group': 'red',
#         'some_other_group': 'green'
#     })

# fig = px.bar(df, x="Indicator", y="Cases", color="Country", barmode="group")
df.plot()
#bar graph
fig1 = px.bar(df, x="Indicator", y="Cases", barmode="group",color="Country",
              # color_discrete_map={'USA':'green',
              #                     'India':'pink',
              #                     })
              color_discrete_sequence=["darkcyan", "deepskyblue","turquoise"],template="plotly_dark"#,width =12
              )
# color_discrete_sequence
# The 'color' property is a color and may be specified as:
#   - A hex string (e.g. '#ff0000')
#   - An rgb/rgba string (e.g. 'rgb(255,0,0)')
#   - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
#   - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
#   - A named CSS color:
#         aliceblue, antiquewhite, aqua, aquamarine, azure,
#         beige, bisque, black, blanchedalmond, blue,
#         blueviolet, brown, burlywood, cadetblue,
#         chartreuse, chocolate, coral, cornflowerblue,
#         cornsilk, crimson, cyan, darkblue, darkcyan,
#         darkgoldenrod, darkgray, darkgrey, darkgreen,
#         darkkhaki, darkmagenta, darkolivegreen, darkorange,
#         darkorchid, darkred, darksalmon, darkseagreen,
#         darkslateblue, darkslategray, darkslategrey,
#         darkturquoise, darkviolet, deeppink, deepskyblue,
#         dimgray, dimgrey, dodgerblue, firebrick,
#         floralwhite, forestgreen, fuchsia, gainsboro,
#         ghostwhite, gold, goldenrod, gray, grey, green,
#         greenyellow, honeydew, hotpink, indianred, indigo,
#         ivory, khaki, lavender, lavenderblush, lawngreen,
#         lemonchiffon, lightblue, lightcoral, lightcyan,
#         lightgoldenrodyellow, lightgray, lightgrey,
#         lightgreen, lightpink, lightsalmon, lightseagreen,
#         lightskyblue, lightslategray, lightslategrey,
#         lightsteelblue, lightyellow, lime, limegreen,
#         linen, magenta, maroon, mediumaquamarine,
#         mediumblue, mediumorchid, mediumpurple,
#         mediumseagreen, mediumslateblue, mediumspringgreen,
#         mediumturquoise, mediumvioletred, midnightblue,
#         mintcream, mistyrose, moccasin, navajowhite, navy,
#         oldlace, olive, olivedrab, orange, orangered,
#         orchid, palegoldenrod, palegreen, paleturquoise,
#         palevioletred, papayawhip, peachpuff, peru, pink,
#         plum, powderblue, purple, red, rosybrown,
#         royalblue, rebeccapurple, saddlebrown, salmon,
#         sandybrown, seagreen, seashell, sienna, silver,
#         skyblue, slateblue, slategray, slategrey, snow,
#         springgreen, steelblue, tan, teal, thistle, tomato,
#         turquoise, violet, wheat, white, whitesmoke,
#         yellow, yellowgreen
#   - A number that will be interpreted as a color
#     according to bar.marker.colorscale
#   - A list or array of any of the above




fig1.update_layout(showlegend=True)
fig1.update_layout(legend = dict(bgcolor = 'black'))
fig1.update_layout({
'plot_bgcolor': 'rgba(250, 250, 250, 250)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})
#Pie graph
fig1.update_traces(base="lines", hovertemplate= 'Date = %{x} <br>' + 'Price = £%{y:.2f}')
fig2 =px.pie(df,names ="Country",values ="Cases",
             color_discrete_sequence=["orange", "red","indianred"],
             hover_name='Country',
             )

fig2.update_layout(showlegend=True)
fig2.update_layout(legend = dict(bgcolor = 'black'))
fig2.update_layout({
'plot_bgcolor': 'rgba(110, 30, 20, 80)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})


#scatter
fig3 =px.scatter(df,x ="Country",y ="Cases",template ="plotly_dark",
                 color ="Country",size='Cases', size_max=60,hover_name='Country',
                #facet_col='Indicator',#facet_col = shows 2 graph....recvoered and total cases
                # , log_x=True  .....change scale of graph
                #color_discrete_sequence=["orange", "red","hotpink"],
                 # animation_frame='Year',
                 # animation_group='Country',#range_x=[100, 45111326], range_y=[25,45111326],
                 labels=dict(Country="Country Name", Cases="Cases", Year="Year")
                 )

fig3.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=["type", "scatter"],
                    label="Scatter Plot",
                    method="restyle"
                ),
                dict(
                    args=["type", "bar"],
                    label="Bar Chart",
                    method="restyle"
                ),
                dict(
                    args=["type", "scatter"],
                    label="PIE Chart",
                    method="restyle"
                ),
                dict(
                    args=["type", "pie"],
                    label="PIE Chart",
                    method="restyle"
                )
            ]),
            direction="down",
        ),
    ]
),
# fig3.update({'layout': {'xaxis': {'color': 'pink'}}})
# fig3.update_layout(showlegend=True)
# fig3.update_layout(legend = dict(bgcolor = 'black')) 
# fig3.update_layout({
# 'plot_bgcolor': 'rgba(250, 250, 250, 250)',
# 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
# })
fig3.update_layout(
    title_text='Average House Price in UK (£)',  
            #plot_bgcolor= 'rgb(194, 208, 209)',
            xaxis_showgrid=False,
            yaxis_showgrid=False,
    hoverlabel=dict(font_size=20, bgcolor='rgb(69, 95, 154)',
           bordercolor= 'whitesmoke'),
    # legend=dict(title='Please click legend item to remove <br>or add to plot',
    #                     x=0,
    #                     y=1,
    #                     traceorder='normal',
      #                     bgcolor='LightSteelBlue',
    #                     xanchor = 'auto'),  
    )
#Line
fig4 =px.line(df,x ="Cases",y ="Country",template ="plotly_dark")

fig4.update_layout(showlegend=True)
fig4.update_layout(legend = dict(bgcolor = 'black'))
fig4.update_layout({
'plot_bgcolor': 'rgba(250, 250, 250, 250)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})

fig5 = px.box(df,x="Indicator",y ="Cases",template ="plotly_dark")

fig5.update_layout(showlegend=True)
fig5.update_layout(legend = dict(bgcolor = 'black'))
fig5.update_layout({
'plot_bgcolor': 'rgba(250, 250, 250, 250)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})

# #scatter
fig6 =px.scatter(df,x ="Country",y ="Cases",template ="plotly_dark",
                  color ="Country",size='Cases', size_max=60,hover_name='Country',
                #facet_col='Indicator',#facet_col = shows 2 graph....recvoered and total cases
                # , log_x=True  .....change scale of graph
                #color_discrete_sequence=["orange", "red","hotpink"],
                  animation_frame='Year',
                  animation_group='Country',#range_x=[100, 45111326], range_y=[25,45111326],
                  labels=dict(Country="Country Name", Cases="Cases", Year="Year")
                  )
fig6.update({'layout': {'xaxis': {'color': 'pink'}}})
fig6.update_layout(showlegend=True)
fig6.update_layout(legend = dict(bgcolor = 'black')) 
fig6.update_layout({
'plot_bgcolor': 'rgba(250, 250, 250, 250)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})   

import plotly.graph_objects as go
fig = go.Figure()

fig.add_trace(go.Indicator(
    value = 200,
    delta = {'reference': 160},
    gauge = {
        'axis': {'visible': False}},
    domain = {'row': 0, 'column': 0}))


fig.add_trace(go.Indicator(
    value = 120,
    gauge = {
        'shape': "bullet",
        'axis' : {'visible': False}},
    domain = {'x': [0.05, 0.5], 'y': [0.15, 0.35]}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 300,
    domain = {'row': 0, 'column': 1}))

fig.add_trace(go.Indicator(
    mode = "delta",
    value = 40,
    domain = {'row': 1, 'column': 1}))

fig.update_layout(
    grid = {'rows': 2, 'columns': 2, 'pattern': "independent"},
    template = {'data' : {'indicator': [{
        'title': {'text': "Speed"},
        'mode' : "number+delta+gauge",
        'delta' : {'reference': 90}}]
                          }})

app =dash.Dash()

app.layout = html.Div(
    style ={
    "backgroundColor":"#111111",
    "textAlign":"Center",
    },children =[
    
    html.Div(
            "Hello",
            style ={
                "color":"white",
                "backgroundColor":"#000021",
                "textAlign":"Center"
                },
        ),
    html.H1("I'm Taral Mehta",
            style ={
                "color":"white",
                "backgroundColor":"#78865",
                "textAlign":"Center",
                }),

    dcc.Dropdown(id ="dropdown",
                 style ={
                     "backgroundColor":"Pink",
                     "textAlign":"Center",
                     "color":"Green",
                     },
        options = [
            {
                'label':"USA",
                'value':100
            },
            {
                "label":"India",
                'value':70
            },
            {
                'label':"Russia",
                'value':40
            }
            ],
            value = 70,
       ),
    html.Br(),
    dcc.Graph(
        id ="graph1",
         figure= fig1,
        ),
    dcc.Graph(
        id ="graph2",
         figure= fig2,
        ),
    dcc.Graph(
        id ="graph3",
         figure= fig3,
        ),
    dcc.Graph(
        id ="graph4",
         figure= fig4,
        ),
    dcc.Graph(
        id ="graph5",
         figure= fig5,
        ),
    dcc.Graph(
        id ="graph6",
         figure= fig6,
        ),
    dcc.Graph(
        id ="graph7",
         figure= fig,
        ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(id="output_file",
             style ={
                 "backgroundColor":"Pink",
                 "textAlign":"Center",
                 "color":"Red",
                 "fontSize":20
                 }
             ),
    # html.Div(id ="output_file2",
    #             style ={
    #                 "backgroundColor":"Pink",
    #                 "textAlign":"Center",
    #                 "color":"Red",
    #                 "fontSize":20
    #                 }
    #          )
    html.Div(
    html.Label("********************************Slider********************************")),
    # dcc.Slider(min=-10,
    #            max=10,
    #            step=0.5,
    #            value=0,
    #            marks={i: "{}".format(i)
    #                   for i in range(-10, 11)}),
    # html.Label("Radio"),
    # dcc.RadioItems(options=[{
    #     "label": "New York City",
    #     "value": "NYC"
    # }, {
    #     "label": "San Francisco",
    #     "value": "SF"
    # }],
    #                value="SF")
    ]
 )

@app.callback(
     Output(component_id ="output_file",component_property="children"),
     [Input(component_id ="dropdown",component_property="value")]
    )
def basic_callback(input_value):
    return input_value

# def basic_callback(value):
#     if value=='Excellent':
#         # xx=['North indian','chinese','continental','cafe','fast food','south indian','italian','desserts','biryani','beverages']
#         # y1=x1
#         col='lightcoral'
#     if value=='Good':
#         # xx=['pasta','burgers',   'cocktails','pizza','biryani','coffee','mocktails','sandwiches','paratha','noodles']
#         # y1=s1
#         col='skyblue'

if __name__ == '__main__':
    app.run()
        
    
    
    #Create World Map 
# # create a map using line_geo()
# fig = px.line_geo(gapminder.query('year == 2007'), locations='iso_alpha', color='continent', projection='orthographic')
# fig.show() 


# # create a map using choropleth
# fig = px.choropleth(gapminder, locations='iso_alpha', color='lifeExp', hover_name='country', 
#                     animation_frame='year', color_continuous_scale=px.colors.sequential.Plasma, projection='natural earth')
# fig.show() 





