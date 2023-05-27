# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 11:39:40 2022

@author: user
"""

import pandas as pd
import numpy as np
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go

# 1. histogram 
# 2. pie + donut
# 3. bootstrap ---> rows and columns
# 4. Dropdown  
# 5. slider
# 6. Rangeslider
# 7. radio button
# 8. checkbutton
# 9. Indicators
# 10. Data set --> stock market
# **************************1 pie graph ************************

a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig1 =px.pie(values =b,color=c,hover_name=a,
             color_discrete_sequence=["pink","orange","purple"])

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta",
             style ={ 
                 "paddingLeft":"350px",
                 # "display":"flex",   
                 }),
    html.Div(dcc.Graph(figure =fig1),
             style ={ 
                 "display":"row",   
                 })
  ],
    style ={ 
        "backgroundColor":"GOld",
        "textAlign":"Left",
        "width":"800px",
        # "paddingLeft":"350px"
        }
    )
if __name__ =="__main__":
    app.run()
    

# **************************2 Donut graph ************************

a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig1 =px.pie(values =b,color=c,hover_name=a,
             color_discrete_sequence=["pink","orange","purple"],hole=0.4)

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta",
             style ={ 
                 "paddingLeft":"350px",
                 # "display":"flex",   
                 }),
    html.Div(dcc.Graph(figure =fig1),
             style ={ 
                 "display":"row",   
                 })
  ],
    style ={ 
        "backgroundColor":"GOld",
        "textAlign":"Left",
        "width":"800px",
        # "paddingLeft":"350px"
        }
    )
if __name__ =="__main__":
    app.run()    
    
    
#*********************3 histogram Graph****************************
# line graph
a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig1 =px.histogram(x=c, y=b,color =c)


app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta",
             style ={ 
                 "paddingLeft":"350px",
                 # "display":"flex",   
                 }),
    html.Div(dcc.Graph(figure =fig1),
             style ={ 
                 "display":"row",   
                 })
  ],
    style ={ 
        "backgroundColor":"GOld",
        "textAlign":"Left",
        "width":"800px",
        # "paddingLeft":"350px"
        }
    )
if __name__ =="__main__":
    app.run()
    
#*********************4 histogram Graph****************************
# line graph
a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig1 =px.histogram(x=c, y=b,color =c)

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta",
             style ={ 
                 "paddingLeft":"350px",
                 # "display":"flex",   
                 }),
    html.Div(dcc.Graph(figure =fig1),
             style ={ 
                 "display":"row",   
                 })
  ],
    style ={ 
        "backgroundColor":"GOld",
        "textAlign":"Left",
        "width":"800px",
        # "paddingLeft":"350px"
        }
    )
if __name__ =="__main__":
    app.run()
    
    
#*********************5 scatter plot3d Graph***************************
a=[12, 2, 35,4,5,6,5.6,2,7]
b=[1, 22, 3,22,3,647,76,2,2]
c =[46,6,5,10,11,22,33,44,55]
e =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai","Navi Mumbai","Navi Mumbai","Thane","Mumbai"]
d = {"a1" :a,"b1":b,"c1":c,"e1":e}
df =pd.DataFrame(d)
df
# Plotting the figure
fig = px.scatter_3d(df, x = 'a1',
					y = 'b1',
					z = 'c1',
 					color = "e1")

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
 

# ******************************  rows and columns with bootstrap *******************************
app =dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
        dbc.Row(dbc.Col(html.H1("Hello List",
                           style ={
                               "textAlign":"Center"
                               }
                           ))),
        dbc.Row([dbc.Col(html.H1("Good",
                           # style ={
                           #     "textAlign":"Center"
                           #     },
                           ),width ={"size":4,"offset":"4"},
                         # style ={
                         #       "textAlign":"Center"
                         #       }
                         ),
                dbc.Col(html.H1("Morning",
                                   # style ={
                                   #     "textAlign":"Center"
                                   #     },
                                   ),width ={"size":4},
                                # style ={
                                #        "textAlign":"Center"
                                #        }
                                )],
                               # style ={
                               #        "textAlign":"Right"
                               #        },
                               # className="text-primary text-Center",#blue color font ko
                               className="text-primary text-center p-5",#text center me aayega
              ),
        ]    
    )

if __name__ =="__main__":
    app.run()
# ******************************  Dropdown list    *******************************
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
        children =[dbc.Row(dbc.Col(html.H1("DropDown List"),
                                   width ={"size":4,"offset":4},
                                   style ={"textAlign":"center"},
                                   
                                   ),className ="text-secondary"),
                   dcc.Dropdown(options =[
                       {
                           "label":"India",
                           "Value":"India"
                           },
                       {
                           "label":"Australia",
                           "Value":"Australia"
                           },
                       {
                           "label":"England",
                           "Value":"England"
                           }
                       
                       ])
                   
                   ]    
    )


if __name__ =="__main__":
    app.run()

# ******************************  Radio Button     ********************************
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
        children =[dbc.Row(dbc.Col(html.H1("Radio Button List"),
                                   width ={"size":4,"offset":4},
                                   style ={"textAlign":"center"},
                                   
                                  className ="text-secondary")),
                   dcc.RadioItems(options =[
                       {
                           "label":"Male",
                           "value":"Male"
                           },
                       {
                           "label":"Female",
                           "value":"Female"
                           },
                       ],
                       value ="Male")
                   ]    
    )

if __name__ =="__main__":
    app.run()

# ******************************  CheckButton      ********************************
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
        children =[dbc.Row(dbc.Col(html.H1("Check Button"),
                                   width ={"size":4,"offset":4},
                                   style ={"textAlign":"center"},
                                   
                                  className ="text-secondary")),
                   dcc.Checklist(options =[
                       {
                           "label":"2015",
                           "value":"2015"
                           },
                       {
                           "label":"2016",
                           "value":"2017"
                           },
                       ],
                       value ="2015")
           ]    
    )

if __name__ =="__main__":
    app.run()


# ******************************  Slider ********************************
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
a=[12, 2, 35,4,5,6,5.6,2,7]
b=[1, 22, 3,22,3,647,76,2,2]
c =[46,6,5,10,11,22,33,44,55]
e =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai","Navi Mumbai","Navi Mumbai","Thane","Mumbai"]
d = {"a1" :a,"b1":b,"c1":c,"e1":e}
df =pd.DataFrame(d)
df
df["a1"].min()
app.layout = html.Div(
        children =[dbc.Row(dbc.Col(html.H1("Slider"),
                                   width ={"size":4,"offset":4},
                                   style ={"textAlign":"center"},
                                   
                                  className ="text-secondary")),
                   dbc.Row(dbc.Col(
    
                       dcc.Slider(min =df["a1"].min(),
                                  max =df["a1"].max(),
                                  step=1
                                  )
                       )
                   )
           ]    
    )

if __name__ =="__main__":
    app.run()

# ******************************  Indicator ********************************
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
a=[12, 2, 35,4,5,6,5.6,2,71]
b=[1, 22, 3,22,3,647,76,2,2]
c =[46,6,5,10,11,22,33,44,55]
e =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai","Navi Mumbai","Navi Mumbai","Thane","Mumbai"]
d = {"a1" :a,"b1":b,"c1":c,"e1":e}
df =pd.DataFrame(d)
df
df["a1"].min()

fig0= go.Figure(go.Indicator(
    value = int(df["a1"].tail(1)),
    mode = "gauge+number",
    delta = {'reference': 160},
    gauge = {
        'axis': {'visible': True}},
    ))


app.layout = html.Div(
        children =[dbc.Row(dbc.Col(html.H1("Slider"),
                                   width ={"size":4,"offset":4},
                                   style ={"textAlign":"center"},
                                   
                                  className ="text-secondary")),
                   dbc.Row(dbc.Col(    
                       dcc.Graph(figure =fig0)
                       )
                   )
           ]    
    )

if __name__ =="__main__":
    app.run()
    
    
  

#******************************** database connectivity   ********************************

import mysql.connector as mysql
import pandas as pd
import pymysql

db_con =mysql.connect(host ="localhost",user="root",passwd ="root",database ="sms1")

# optional Part
# my_cur =db_con.cursor()
# my_cur.execute("use abc;")
# my_cur.execute("select * from stud_db;")
# for x in my_cur:
#     print(x)
    
query = 'select * from apple_stock'
df = pd.read_sql(query, con = db_con)
print(df)


# *********************** Stock Market *************************************************

import pandas as pd 
import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import datetime as dt
import pandas_datareader.data as web 


df = pd.read_csv(r"https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv",parse_dates=["Date"])
df =pd.read_csv(r"C:\Users\user\Downloads\apple_stock.csv")
df
df.to_csv()
df.info()
df.isnull().sum()
df["Year"] = df.Date.dt.year
df
df["Year"] =df.Year.astype(str)
df.info()
df["Month"] = df.Date.dt.month
df
df1_copy = df.copy() 
df1_copy

df1_copy.Month.unique()
df1_copy.sort_values("Month",inplace=True)
df1_copy["Month_in_Word"] = df1_copy.Month.astype(str)
df1_copy.info()
df1_copy.Month_in_Word.replace(
                 {"1":"January",
                  "2":"February",
                  "3":"March",
                  "4":"April",
                  "5":"May",
                  "6":"June", 
                  "7":"July",
                  "8":"August",
                  "9":"September",
                  "10":"October",
                  "11":"November",
                  "12":"December",
                  },inplace=True)
df
df1_copy
df.info()


app =dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

fig5 =go.Figure()
fig5.add_scattergl(x=df["Date"], y=df["AAPL.Close"],line={'color': 'black'})

# Full line
fig5.add_scattergl(x=df["Date"], y=df["AAPL.Close"].where(df["AAPL.Close"] <=115), 
                    line={'color': 'red'})

# Above threshhgold    
fig5.add_scattergl(x=df["Date"],y=df["AAPL.Close"].where(df["AAPL.Close"] >115),
                  line={'color': 'green'})


fig5.update_traces(mode="markers+lines",   
                   hovertemplate="%{y}%{_xother}")#hovertemplate="AAPL.Close")
# fig5.update_layout(hovermode="x")
# fig5.update_layout(hovermode="closest")
fig5.update_layout(hovermode="x unified")
fig5.update_layout(height=700,width=1000)

# # Full line
# fig5.add_scattergl(x=df["Date"], y=df["AAPL.Close"].where(df.direction =="Decreasing"), 
#                    line={'color': 'black'})

# # Above threshhgold
# fig5.add_scattergl(x=df["Date"],y=df["AAPL.Close"].where(df.direction =="Increasing"),
#                   line={'color': 'red'})
fig6 = go.Figure()

fig6.add_trace(go.Bar(
    x=df["Date"],
    y=df["AAPL.Close"],
    # xperiod="M3",
    # xperiodalignment="middle",
    # xhoverformat="Q%q",
    hovertemplate="%{y}"
))

fig6.add_trace(go.Scatter(
    x=df["Date"],
    y=df["AAPL.Low"],
    # xperiod="M1",
    # xperiodalignment="middle",
    hovertemplate="%{x}"
))


# app.layout =dbc.Container(
app.layout =html.Div(
    [
    dbc.Row([
            dbc.Col(html.H6("Stock Market Dashboard1", 
                            style ={"textAlign":"Right"},
                            #className='text-center'
                            ),
               width ={'size':4,'offset':1, 'order':2},
               ),
            dbc.Col(html.H6("Stock Market Dashboard2", 
                            #className='text-center',
                            style ={"textAlign":"Right"}
                            ),
                width={'size':4, 'offset':1, 'order':1},
                ),
            ]),
    # Horizontal:start,center,end,between,around
    # style={"width": "6rem"},
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id ="dropdown1",
                options = [{
                    "label":"AAPL.Open",
                    "value":"AAPL.Open"
                    },
                {
                    "label":"AAPL.High",
                    "value":"AAPL.High"   
                    },
               
                {
                    "label":"AAPL.Low ",
                    "value":"AAPL.Low"
                    },
               
                {
                    "label":"AAPL.Close",
                    "value":"AAPL.Close",
                   
                    }],multi =True),
        ], width={'size':2, 'offset':1, 'order':1},
            #xs=12, sm=12, md=12, lg=5, xl=5
        ),

        dbc.Col(
            dcc.Dropdown(id ="dropdown2",
                options = [{
                    "label":"AAPL.Open",
                    "value":"AAPL.Open"
                    },
                {
                    "label":"AAPL.High",
                    "value":"AAPL.High"   
                    },
               
                {
                    "label":"AAPL.Low ",
                    "value":"AAPL.Low"
                    },
               
                {
                    "label":"AAPL.Close",
                    "value":"AAPL.Close",
                    "disabled":True
                     
                    }] ),
            width={'size':2, 'offset':1, 'order':2},
            #xs=12, sm=12, md=12, lg=5, xl=5,
        ),
    dbc.Col(
        dcc.Dropdown(id ="dropdown3",
            options = [
            {
                "label":"2015",
                "value":"2015"
                },
            {
                "label":"2016",
                "value":"2016"
                },
            {
                "label":"2017",
                "value":"2017"
                },
            ] ),
        width={'size':2, 'offset':1, 'order':3},
        #xs=12, sm=12, md=12, lg=5, xl=5,
    ),
    dbc.Col(
        dcc.Dropdown(id ="dropdown4",
            options = [
            {
                "label":"Increasing",
                "value":"Increasing"
                },
            {
                "label":"Decreasing",
                "value":"Decreasing"
                },
            ] ),
        width={'size':2, 'offset':1,"order":4},
        #xs=12, sm=12, md=12, lg=5, xl=5,
    )
    ]),
    dbc.Row(dbc.Col(dcc.RadioItems(
            style ={
            "backgroundColor":"white",
            "textAlign":"Right"
            },
        id='radio_items',
        options=[
            {'label': 'Increasing', 'value': 'Increasing'},
            {'label': 'Decreasing', 'value': 'Decreasing'},
        ],
        value='Decreasing'
    ),width ={'size':2, "offset":2,"order":5})),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id="linegraph0"),width ={'size':6}),
        dbc.Col(dcc.Graph(id="linegraph1"),width ={'size':6}),
        ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="linegraph2"),width ={'size':6}),
        dbc.Col(dcc.Graph(id="linegraph3"),width ={'size':6}),  
        ]),
    dbc.Row(dbc.Col(
        dcc.Checklist(id='my_checklist',# used to identify component in callback
               options=[
                        {'label': "2015", 'value': "2015", 'disabled':False},
                        {'label': "2016", 'value': "2016", 'disabled':False},
                        {'label': "2017", 'value': "2017", 'disabled':False},
                        {'label': "2018", 'value': "2018", 'disabled':True}
               ],
               # value=['2019'],    
               inputStyle={'cursor':'pointer'},      # style of the <input> checkbox element
               style ={
               "backgroundColor":"lightblue"
               },
            ),
        )),
    dbc.Row(dbc.Col(
        dcc.Checklist(id='my_checklist2',# used to identify component in callback
                options=[
                         {'label': "January", 'value':"1", 'disabled':False},
                         {'label': "February", 'value':"2", 'disabled':False},
                         {'label': "March", 'value':"3", 'disabled':False},
                         {'label': "April", 'value':"4", 'disabled':False},
                         {'label': "May", 'value':"5", 'disabled':False},
                         {'label': "June", 'value':"6", 'disabled':False},
                         {'label': "July", 'value':"7", 'disabled':False},
                         {'label': "August", 'value':"8", 'disabled':False},
                         {'label': "September", 'value':"9", 'disabled':False},
                         {'label': "October", 'value':'10', 'disabled':False},
                         {'label': "November", 'value':"11", 'disabled':False},
                         {'label': "December", 'value':"12", 'disabled':False}
                         # for x in df['Month Call Made'].unique()
                ],
               # value=['2019'],    
               inputStyle={'cursor':'pointer'},      # style of the <input> checkbox element
               style ={
               "backgroundColor":"lightpink"
               },
            ),
        )),
    dbc.Row(dbc.Col([dbc.Card(dbc.CardImg(src =r"/static/images/lokesh.jpg")),
                     dbc.CardBody(html.Label("Hellllllllllo"))],width="auto")),
    
    dbc.Row(dbc.Col([html.Label("Date :-"),
            dcc.DatePickerRange(id ="date_pick_range",
            start_date_placeholder_text="Start Period",
            end_date_placeholder_text="End Period",
            calendar_orientation='vertical',
            display_format='DD/MM/YYYY',
            start_date = dt.datetime(2015, 1, 1),
            end_date = dt.datetime(2017, 12, 31),
            min_date_allowed = dt.datetime(2015, 1, 1),
            max_date_allowed = dt.datetime(2017, 12, 31),
            initial_visible_month =dt.datetime(2017, 1, 31)
)]
        
        )),
    dbc.Row([
        dbc.Col(dcc.Graph(id="linegraph4"),width ={'size':6}),
        ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="linegraph5"),width ={'size':6}),
        ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="linegraph6",figure =fig5),width ={'size':6}),
        ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="linegraph7",figure =fig6),width ={'size':6}),
        ]),
      ])  
  

@app.callback(
    Output("linegraph0", "figure"), 
    Input("dropdown1", "value"))

def display_time_series(dropdown):
    fig0 = px.line(df, x='Date', y=dropdown, title =" Date vs  GRaph")
    return fig0


@app.callback(
    Output("linegraph1", "figure"), 
    Input("dropdown2", "value"),
    Input("dropdown3", "value"))

def display_time_series(dropdown2,dropdown3):
    dff =df[df["Year"]==dropdown3]
    fig1 = px.line(dff, x="Date", y =dropdown2,title =" GRaph vs  GRaph")
    return fig1


@app.callback(
    Output("linegraph2", "figure"), 
    Input("radio_items", "value"),
    )

def radio_button_update(r_button_value):
    print("=============")
    print(r_button_value)
    print("=============")
    # df[df["direction"] == "Decreasing"] ---- it shows whole data frame
    df_filter1 = df[df["direction"] == r_button_value]
    fig2 = px.line(df_filter1, x=df_filter1["Date"], y=df_filter1["AAPL.Low"],title =" Date vs  Low")
    return fig2

#line chart
@app.callback(
    Output("linegraph3", "figure"), 
    Input("my_checklist", "value"),
    )
    
def line_update(options_chosen):
    print("=============")
    print(options_chosen)      
    print("=============")
    # df[df["Year"] == 2015] ---- it shows whole data 
    x = df.Year.unique()
    x
    df_filter2 = df[df["Year"].isin(options_chosen)]
    print ("**************",df_filter2['Year'].unique(),"********")
    fig3 = px.pie(df_filter2, values ="AAPL.Low",hole =0.4)
    return fig3


@app.callback(
    Output("linegraph4", "figure"), 
    Input("my_checklist2", "value"))

def month_wise_graph(options_chosen):
    print("***********Month is word******************",options_chosen)
    df_filter_v1 = df1_copy[df1_copy['Year']=='2015']
    df_filter_v1["Month"]=df_filter_v1.Month.astype(str)
    df_filter_v1["Month"]    
    df_filter3 =df_filter_v1[df_filter_v1["Month"].isin(options_chosen)]
    fig4 = px.bar(df_filter3, x="Date", y="AAPL.Low", title =" Month vs  GRaph")
    return fig4
    

# @app.callback(
#     Output('linegraph5', 'figure'),
#     [Input('date_pick_range', 'start_date'),
#      Input('date-date_pick_range-range', 'end_date')
#      ])
# def date_graph(start_date, end_date):
#     print("=============")
#     print(start_date,end_date)
#     print("=============")
#     # df[df["direction"] == "Decreasing"] ---- it shows whole data frame
#     df_filter4 = df[(df["Date"] > start_date) &(df["Date"] < end_date)]
#     fig5 = px.line(df_filter4, x=df_filter4["Date"], y=df_filter4["AAPL.Low"],title =" Date pickerGraph")
#     return fig5

if  __name__ =="__main__":
    app.run()   

























