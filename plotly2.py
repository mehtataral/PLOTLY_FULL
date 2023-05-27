# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 15:23:43 2022

@author: user
"""
    
#******************************************************************************** 

import dash     
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd   
import dash_bootstrap_components as dbc
d ={
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["Mumbai", "Mumbai", "Mumbai", "Thane", "Thane", "Thane"]
}  
df = pd.DataFrame(d)
df
app =dash.Dash() 
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''Dash: A web application framework for your data.'''),
    dcc.Graph(
        id='example-graph',
        figure=fig
        ),
    dcc.Dropdown( id = 'dropdown',
    options = [
        {'label':'Google', 'value':'GOOG' },
        {'label': 'Apple', 'value':'AAPL'},
        {'label': 'Amazon', 'value':'AMZN'},
        ],
    value = 'GOOGL'       
    )
])
if __name__ == '__main__':
    app.run()
    
    
#********************************************************************************    
    
    
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc

app =dash.Dash()
app.layout =html.Div(children =[
    html.H1("Hello Taral Mehta"),
    html.H2("Byeeee!!!!!!")

    ])

if __name__ =="__main__":
    app.run()


    
#********************************************************************************    
    
    
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc

app =dash.Dash()
app.layout =html.Div([
    html.H1("Hello Taral Mehta"),
    html.H2("Byeeee!!!!!!"),
    dbc.Row(dbc.Col(html.Div("A single column"))),
    dbc.Row(dbc.Col(html.H1("A single column"))),
    dbc.Row(dbc.Col(html.H2("A single column"))),

    ])

if __name__ =="__main__":
    app.run()
    
#********************************************************************************    
 

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc
app =dash.Dash()

app.layout = html.Div(children=[
   html.H1(children='Hello Dash'),
   html.Div(children='''Dash Framework: A web application framework for Python.''')
   ])

if __name__ =="__main__":
    app.run()

#********************************************************************************    

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc

app= dash.Dash()
colors = {
    'background': '#87D693',
    'text': '#ff0033'
}
app.layout =html.Div(
    
    style={
          'backgroundColor': colors['background']
          }, 
    
    children =[
        html.H1(
            children = "Hello",
            style={
                      'textAlign': 'left',
                      'color': colors['text']
                }),
        
        html.H2("Byeee"),
        
        html.Div(
            children ="Learning plotly........",
            style={
                  'textAlign': 'right',
                  'color': colors['text']
              }
         ) 
    ])

if __name__ =="__main__":
    app.run()

#********************************************************************************    
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc

app = dash.Dash()
colors = {
    'background': '#87D653',
    'text': '#ff0033'
}
app.layout =html.Div([
    html.H1("Hi"),    
    html.H2("Byeee"),
    html.Div("Learning plotly again........"),
    html.H1("hsafaf",
         style={
         "color" :"red"
        }),
    html.H2("kjhlksJ",
        style = {
            "backgroundColor":colors['background']
            }
        )
    ])

if __name__ =="__main__":
    app.run()
    
#********************************************************************************    
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import pandas as pd
# import dash_bootstrap_components as dbc

# app =dash.Dash()
# app.layout =html.Div([
#     html.H1("Hi"),    
#     html.H2("Byeee"),
#     html.Div("Learning plotly again........"),
    

#     # figure (dict; default {    data: [],    layout: {},    frames: [],}):
#     #     Plotly `figure` object. See schema:
#     #     https://plotly.com/javascript/reference  `config` is set
#     #     separately by the `config` property.

#     #     `figure` is a dict with keys:

#     #     - data (list of dicts; optional)

#     #     - frames (list of dicts; optional)

#     #     - layout (dict; optional)
#     dcc.Graph(
#       id='example_graph_ka',
#       figure={
#          'data': [
#             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Delhi'},
#             {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Mumbai'},
#          ],
#          'layout': {
#             'title': 'Dash Data Visualization'
#          }
#       }
#    )
#  ])

# if __name__ =="__main__":
#     app.run()
    
#******************************************************************************
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import pandas as pd
# import dash_bootstrap_components as dbc

# app = dash.Dash()
# colors = {
#    'background': '#87D653',
#    'text': '#ff0033'
# }

# app.layout = html.Div(
#    style={
#        'backgroundColor': colors['background']
#        }, 
#    children=[
#    html.H1(
#       children='Hello Dash',
#       style={
#          'textAlign': 'center',
#          'color': colors['text']
#              }
#            ),
# 	
#    html.Div(
#        children='Dash: A web application framework for Python.', 
#        style={
#       'textAlign': 'center',
#       'color': colors['text']
#    }
#    ),
# 	
#    dcc.Graph(
#       id='example-graph-2',

#       figure={
#          'data': [
#             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Delhi'},
#             {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Mumbai'},
#          ],
#          'layout': {
#             'plot_bgcolor': colors['background'],
#             'paper_bgcolor': colors['background'],
#             'font': {
#                'color': colors['text']
#             }
#          }
#       }
#    )
# ])
    
# if __name__ =="__main__": 
#     app.run()  
#***************************************************************************** 
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


app = dash.Dash()
    
app.layout = html.Div([
            html.H1(
                    "Hello Guysss....",
                    style = {
                            "color" :"red",
                            "textAlign" :"right",
                            "backgroundColor":"pink"
                            
                        }
                ) ,
            
            html.H2(
                    "Byee Guysss....",
                    style = {
                            "color" :"blue",
                            "textAlign" :"left",
                            "backgroundColor":"green"
                            
                        }
                ) 
    ])   
if __name__ =="__main__":
    app.run()
    
#****************************************************************************
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd 



d ={
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["Mumbai", "Mumbai", "Mumbai", "Thane", "Thane", "Thane"]
}  
df = pd.DataFrame(d)
df
app = dash.Dash()
    
app.layout = html.Div([
            html.H1(
                    "Hello Guysss....",
                    style = {
                            "color" :"red",
                            "textAlign" :"right",
                            "backgroundColor":"pink"
                            
                        }
                ) ,
            
            html.H2(
                    "Byee Guysss....",
                    style = {
                            "color" :"blue",
                            "textAlign" :"left",
                            "backgroundColor":"green"
                            
                        }
                ) 
    ])   
if __name__ =="__main__":
    app.run()
   


#****************************************************************************
import dash     
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
  

d ={
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["Mumbai", "Mumbai", "Mumbai", "Thane", "Thane", "Thane"]
}  
df = pd.DataFrame(d)
df

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
# fig = px.bar(df, x="Fruit", y="Amount",color="City", barmode="relative")
# fig = px.bar(df, x="Fruit", y="Amount",color="City", barmode="overlay")


app= dash.Dash()
app.layout = html.Div(children=[
    html.H1(
        children='Hello Dash',
       ),
    
    html.Div(
        children='''Dash: A web application framework for your data.''',
        ),
    dcc.Graph(
        id='example-graph',
        figure=fig
        )
])
if __name__ == '__main__':
    app.run()         
    
#****************************************************************************
import dash     
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
  

d ={
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["Mumbai", "Mumbai", "Mumbai", "Thane", "Thane", "Thane"]
}  
df = pd.DataFrame(d)
df

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
# fig = px.bar(df, x="Fruit", y="Amount",color="City", barmode="relative")
# fig = px.bar(df, x="Fruit", y="Amount",color="City", barmode="overlay")

app= dash.Dash()
app.layout = html.Div(children=[
    html.H1(
        children='Hello Dash',
        style={
            'color':"red",
            "textAlign":"center",
            "backgroundColor":"Silver"
            }),
    
    html.Div(
        children='''Dash: A web application framework for your data.''',
        style={
            'color':"white",
            "backgroundColor":"Gold"
            }
        ),
    dcc.Graph(
        id='example-graph',
        figure=fig
        )
])
if __name__ == '__main__':
    app.run()       
#*****************************************************************************
import dash     
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px


# Creating the Figure instance
fig = px.line(x =[11, 42, 33],y =[1, 2, 3])
app =dash.Dash()
# printing the figure instance
app.layout =html.Div([
        html.H1("line Graph"),
        dcc.Graph(
            figure =fig
            )
    ])
print(fig)
fig.show()
if __name__ == "__main__":
    app.run()
    

#*****************************************************************************
import dash     
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd
a=[12, 2, 35]
b=[1, 22, 3]
d = {"a1" :a,"b1":b}
df =pd.DataFrame(d)
df
# Creating the Figure instance
fig = px.line(df,x ="a1",y="b1")
# fig = px.line(df)

app =dash.Dash()
# printing the figure instance
app.layout =html.Div([
        html.H1("line Graph"),
        dcc.Graph(
            figure =fig
            )
    ])
print(fig)
fig.show()
if __name__ == "__main__":
    app.run()
    
#*****************************************************************************
import dash     
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd


a=[12, 2, 35]
b=[1, 22, 3]
d = {"a1" :a,"b1":b}
df =pd.DataFrame(d)
df
# Creating the Figure instance
fig = px.bar(df,x ="a1",y="b1", barmode="group",color ="a1")
# fig = px.line(df)

app =dash.Dash()
# printing the figure instance
app.layout =html.Div([
        html.H1("line Graph"),
        dcc.Graph(
            figure =fig
            )
    ])
print(fig)
fig.show()
if __name__ == "__main__":
    app.run()
    

#*****************************************************************************
import dash     
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd


a=[12, 2, 35]
b=[1, 22, 3]
d = {"a1" :a,"b1":b}
df =pd.DataFrame(d)
df
# Creating the Figure instance
fig = px.scatter(df,x ="a1",y="b1")
# fig = px.scatter(df)

app =dash.Dash()
# printing the figure instance
app.layout =html.Div([
        html.H1("scatter Graph"),
        dcc.Graph(
            figure =fig
            )
    ])
print(fig)
fig.show()
if __name__ == "__main__":
    app.run()



#*****************************************************************************


import dash     
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd


a=[12, 2, 35]
b=[1, 22, 3]
d = {"a1" :a,"b1":b}
df =pd.DataFrame(d)
df
# Creating the Figure instance
fig = px.pie(df,values ="a1",names ="b1")
# fig = px.scatter(df)

app =dash.Dash()
# printing the figure instance
app.layout =html.Div([
        html.H1("Pie Graph"),
        dcc.Graph(
            figure =fig
            )
    ])
print(fig)
fig.show()
if __name__ == "__main__":
    app.run()


#********************************************************************************

import dash     
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd


a=[12, 2, 35]
b=[1, 22, 3]
d = {"a1" :a,"b1":b}
df =pd.DataFrame(d)
df
# Creating the Figure instance
fig = px.box(df,x="a1",y ="b1")
# fig = px.scatter(df)

app =dash.Dash()
# printing the figure instance
app.layout =html.Div([
        html.H1("Box Graph"),
        dcc.Graph(
            figure =fig
            )
    ])
print(fig)
fig.show()
if __name__ == "__main__":
    app.run()


#********************************************************************************

import dash     
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd


a=[12, 2, 35]
b=[1, 22, 3]
d = {"a1" :a,"b1":b}
df =pd.DataFrame(d)
df
# Creating the Figure instance
fig = px.violin(df,x="a1",y ="b1")
# fig = px.scatter(df)

app =dash.Dash()
# printing the figure instance
app.layout =html.Div([
        html.H1("violin Graph"),
        dcc.Graph(
            figure =fig
            )
    ])
print(fig)
fig.show()
if __name__ == "__main__":
    app.run()

#********************************************************************************


import plotly.express as px

# Data to be plotted
df = px.data.iris()



a=[12, 2, 35]
b=[1, 22, 3]
c =[46,6,5]
d = {"a1" :a,"b1":b,"c1":c}
df =pd.DataFrame(d)
df
# Plotting the figure
fig = px.scatter_3d(df, x = 'a1',
					y = 'b1',
					z = 'c1')
# 					color = 'species')

app =dash.Dash()
# printing the figure instance
app.layout =html.Div([
        html.H1("3D Scatter Graph"),
        dcc.Graph(
            figure =fig
            )
    ])
print(fig)
fig.show()
if __name__ == "__main__":
    app.run()


# ***************************************************************************

import plotly.graph_objects as go
import numpy as np
 
# Data to be plotted
x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
y = x.copy().T
z = np.cos(x ** 2 + y ** 2)
 
# plotting the figure
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])
 
app =dash.Dash()
# printing the figure instance
app.layout =html.Div([
        html.H1("3D  Graph"),
        dcc.Graph(
            figure =fig
            )
])
print(fig)
fig.show()
if __name__ == "__main__":
    app.run()



#***************************************************************************


import plotly.express as px

a=[12, 2, 35]
b=[1, 22, 3]
c =[46,6,5]

d = {"a1" :a,"b1":b,"c1":c}
df =pd.DataFrame(d)
df
app =dash.Dash()
# Plotting the figure
fig = px.scatter_3d(df, x = 'a1',
					y = 'b1',
					z = 'c1')
# 					color = 'species')


# printing the figure instance
app.layout =html.Div([
        html.H1("3D Scatter Graph"),
        dcc.Graph(
            figure =fig
            ),
        html.Div(dcc.Dropdown(id='dropdown', 
                options =[{'label':'california','value':'california'},
                          {'label':'illinois', 'value':'illinois'},     
                          {'label':'new york', 'value':'new york'}
                          ]
                           ))
                           
    ])
print(fig)
fig.show()
if __name__ == "__main__":
    app.run()



#******************************************************************************

import mysql.connector as mysql
import pandas as pd
import pymysql

db_con =mysql.connect(host ="localhost",user="root",passwd ="root",database ="abc")

# optional Part
# my_cur =db_con.cursor()
# my_cur.execute("use abc;")
# my_cur.execute("select * from stud_db;")
# for x in my_cur:
#     print(x)
    
query = 'select * from stud_db'
df = pd.read_sql(query, con = db_con)
print(df)






# Importing packages

import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import plotly.express as px
import plotly.graph_objects as go

# Pulling Data

start = dt.datetime(2019,1,1)
end = dt.datetime.now()

stocks = web.DataReader(['FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'], 
                        'yahoo', start, end)

stocks_close = pd.DataFrame(web.DataReader(['FB','AMZN', 'AAPL', 'NFLX', 'GOOGL', 'MSFT'], 
                                           'yahoo', start, end)['Close'])

# Area chart

area_chart = px.area(stocks_close.FB, title = 'FACEBOOK SHARE PRICE (2013-2020)')

area_chart.update_xaxes(title_text = 'Date')
area_chart.update_yaxes(title_text = 'FB Close Price', tickprefix = '$')
area_chart.update_layout(showlegend = False)

area_chart.show()

# Customized chart

c_area = px.area(stocks_close.FB, title = 'FACBOOK SHARE PRICE (2013-2020)')

c_area.update_xaxes(
    title_text = 'Date',
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))

c_area.update_yaxes(title_text = 'FB Close Price', tickprefix = '$')
c_area.update_layout(showlegend = False,
    title = {
        'text': 'FACEBOOK SHARE PRICE (2013-2020)',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

c_area.show()

# Simple candlestick

candlestick = go.Figure(data = [go.Candlestick(x = stocks.index, 
                                               open = stocks[('Open',    'AMZN')], 
                                               high = stocks[('High',    'AMZN')], 
                                               low = stocks[('Low',    'AMZN')], 
                                               close = stocks[('Close',    'AMZN')])])

candlestick.update_layout(xaxis_rangeslider_visible = False, title = 'AMAZON SHARE PRICE (2013-2020)')
candlestick.update_xaxes(title_text = 'Date')
candlestick.update_yaxes(title_text = 'AMZN Close Price', tickprefix = '$')

candlestick.show()

# Customized candlestick

c_candlestick = go.Figure(data = [go.Candlestick(x = stocks.index, 
                                               open = stocks[('Open',    'AMZN')], 
                                               high = stocks[('High',    'AMZN')], 
                                               low = stocks[('Low',    'AMZN')], 
                                               close = stocks[('Close',    'AMZN')])])

c_candlestick.update_xaxes(
    title_text = 'Date',
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))

c_candlestick.update_layout(
    title = {
        'text': 'AMAZON SHARE PRICE (2013-2020)',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
c_candlestick.update_yaxes(title_text = 'AMZN Close Price', tickprefix = '$')

c_candlestick.show()

# Simple OHLC chart

ohlc = go.Figure(data = [go.Ohlc(x = stocks.index, 
                                               open = stocks[('Open',    'AAPL')], 
                                               high = stocks[('High',    'AAPL')], 
                                               low = stocks[('Low',    'AAPL')], 
                                               close = stocks[('Close',    'AAPL')])])

ohlc.update_layout(xaxis_rangeslider_visible = False, title = 'APPLE SHARE PRICE (2013-2020)')
ohlc.update_xaxes(title_text = 'Date')
ohlc.update_yaxes(title_text = 'AAPL Close Price', tickprefix = '$')

ohlc.show()

# Customized OHLC

c_ohlc = go.Figure(data = [go.Ohlc(x = stocks.index, 
                                               open = stocks[('Open',    'AAPL')], 
                                               high = stocks[('High',    'AAPL')], 
                                               low = stocks[('Low',    'AAPL')], 
                                               close = stocks[('Close',    'AAPL')])])

c_ohlc.update_xaxes(
    title_text = 'Date',
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))

c_ohlc.update_layout(
    title = {
        'text': 'APPLE SHARE PRICE (2013-2020)',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
c_ohlc.update_yaxes(title_text = 'AAPL Close Price', tickprefix = '$')

c_ohlc.show()

# Basic bullet chart

bullet_chart = go.Figure(go.Indicator(
    mode = "number+gauge+delta",
    gauge = {'shape': "bullet", 
             'axis': {'range': [None, 600]}},
    value = int(stocks_close['NFLX'].tail(1)),
    delta = {'reference': int(stocks_close['NFLX'].tail(2)[0])},
    domain = {'x': [0, 1], 
              'y': [0, 1]},
    title = {'text':"<b>NETFLIX<br>DAY<br>RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 
             'font': {"size": 16}}))

bullet_chart.update_layout(height = 250)

bullet_chart.show()

# Customized bullet chart

c_bullet = go.Figure()

c_bullet.add_trace(go.Indicator(
    mode = "number+gauge+delta", 
    value = int(stocks_close['NFLX'].tail(1)),
    delta = {'reference': int(stocks_close['NFLX'].tail(2)[0])},
    domain = {'x': [0.25, 1], 
              'y': [0.08, 0.25]},
    title = {'text':"<b>NETFLIX DAY<br>RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 
             'font': {"size": 14}},    
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 550]},
        'threshold': {
            'line': {'color': "Red", 'width': 2},
            'thickness': 0.75,
            'value': 505},
        'steps': [
            {'range': [0, 350], 'color': "gray"},
            {'range': [350, 550], 'color': "lightgray"}],
        'bar': {'color': 'black'}}))

c_bullet.add_trace(go.Indicator(
    mode = "number+gauge+delta", 
    value = int(stocks_close['GOOGL'].tail(1)),
    delta = {'reference': int(stocks_close['GOOGL'].tail(2)[0])},
    domain = {'x': [0.25, 1], 
              'y': [0.4, 0.6]},
    title = {'text':"<b>GOOGLE DAY<br>RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 
             'font': {"size": 14}},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 1800]},
        'threshold': {
            'line': {'color': "red", 'width': 2},
            'thickness': 0.75,
            'value': 1681},
        'steps': [
            {'range': [0, 1300], 'color': "gray"},
            {'range': [1300, 1800], 'color': "lightgray"}],
        'bar': {'color': 'black'}}))

c_bullet.add_trace(go.Indicator(
    mode = "number+gauge+delta", 
    value = int(stocks_close['MSFT'].tail(1)),
    delta = {'reference': int(stocks_close['MSFT'].tail(2)[0])},
    domain = {'x': [0.25, 1], 
              'y': [0.7, 0.9]},
    title = {'text':"<b>MICROSOFT DAY<br>RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 
             'font': {"size": 14}},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 250]},
        'threshold': {
            'line': {'color': "red", 'width': 2},
            'thickness': 0.75,
            'value': 208},
        'steps': [
            {'range': [0, 150], 'color': "gray"},
            {'range': [150, 250], 'color': "lightgray"}],
        'bar': {'color': "black"}}))

c_bullet.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})

c_bullet.show()

# Gauge charts

gauge = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = int(stocks_close['FB'].tail(1)),
    mode = "gauge+number+delta",
    title = {'text':"<b>FACEBOOK DAY RANGE</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 'font': {"size": 20}},
    delta = {'reference': int(stocks_close['FB'].tail(2)[0])},
    gauge = {
             'axis': {'range': [None, 300]},
             'steps' : [
                 {'range': [0, 200], 'color': "lightgray"},
                 {'range': [200, 300], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 
                            'thickness': 0.75, 
                            'value': 276}}))

gauge.show()
# view rawfull_code.py hosted with ❤ by GitHub






















