# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 11:57:03 2022

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

a = [11,22,33,44,55,67,88]
b = [1,2,3,4,5,7,8]

# line
# bar
# pie
# scatter
# area
# histogram
# box
# scatter_3d
# violin
# candlstick
# fig_line = px.line(a)
# fig_line1 = px.line(a,b)
# fig_bar = px.bar(a,b)
# fig_scatter = px.scatter(a,b)
# fig_area = px.area(a,b)
# fig_histogram = px.histogram(a)
# fig_box = px.box(a,b)
# fig_violin = px.violin(a,b)
# fig_scatter_3d = px.scatter_3d(x =a,y =b)


# fig_candlstick = go.Figure(data =[go.Candlestick(x= a)])
# x = dash.Dash()
# x.layout = html.Div(children =[
#     dbc.Row(children =[
#                        dbc.Col("data is ready"),
#                        dbc.Col(dcc.Graph(figure =fig_line1))
#                        ]),
#     dbc.Row(dbc.Col("data is ready",width=3)),
#     dbc.Row(children=[
#             dbc.Col(dcc.Graph(figure =fig_line),width=1),
#             dbc.Col(dcc.Graph(figure =fig_bar)),
#             dbc.Col(dcc.Graph(figure =fig_scatter))]),
#     dbc.Row(dbc.Col(dcc.Graph(figure =fig_area))),
#     dbc.Row(dbc.Col(dcc.Graph(figure =fig_histogram))),
#     dbc.Row(dbc.Col(dcc.Graph(figure =fig_box))),
#     dbc.Row(dbc.Col(dcc.Graph(figure =fig_violin))),
#     dbc.Row(dbc.Col(dcc.Graph(figure =fig_scatter_3d))),
#     dbc.Row(dbc.Col(dcc.Graph(figure =fig_candlstick)))
#     ])

#*********************PART 1****************************


app =dash.Dash()

app.layout = html.Div(children=[
    html.Div("Hello World") ,
    html.Div("My Name is Taral Mehta")
  ]
    )


if __name__ =="__main__":
    app.run()

#*********************PART 2**************************


app =dash.Dash()

app.layout = html.Div(children=[
    html.Div("Hello World") ,
    html.Div("My Name is Taral Mehta")
  ]    ,
    style={"display":"flex"}
    )


if __name__ =="__main__":
    app.run()

#*********************PART 3**************************

app =dash.Dash()

app.layout = html.Div(children=[
    html.Div("Hello World") ,
    html.Div("My Name is Taral Mehta")
  ]    ,
    style={"display":"row"}
    )


if __name__ =="__main__":
    app.run()


#*********************PART 4****************************

app =dash.Dash()

app.layout = html.Div(children=[
    html.Div("Hello World",
             style ={ 
                 "backgroundColor":"GOld",
                 "textAlign":"Right"
                 }) ,
    html.Div("My Name is Taral Mehta")
  ]    ,
    # style={"display":"flex"}
    )


if __name__ =="__main__":
    app.run()


#*********************PART 5****************************

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta"),
  ],
    style ={ 
        "backgroundColor":"GOld",
        "textAlign":"Right"
        }
    )

if __name__ =="__main__":
    app.run()
    
#*********************PART 6****************************

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta"),
  ],
    style ={ 
        "backgroundColor":"GOld",
        "textAlign":"Right",
        "width":"200px"
        }
    )

if __name__ =="__main__":
    app.run()
    
    
#*********************PART 7****************************

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta"),
  ],
    style ={ 
        "backgroundColor":"GOld",
        "textAlign":"Right",
        "width":"800px",
        "display":"flex"
        }
    )

if __name__ =="__main__":
    app.run()
    
    
#*********************PART 8****************************

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta",
             style ={ 
                 "backgroundColor":"GOld",
                 "textAlign":"Right",
                 "width":"800px",
                 "display":"flex"
                 }),
  ],
    )

if __name__ =="__main__":
    app.run()
    
#*********************PART 9****************************

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta",
             style ={ 
                 "paddingLeft":"350px"
                 }),
  ],
    style ={ 
        "backgroundColor":"GOld",
        "textAlign":"Left",
        "width":"800px",
        "display":"flex",   
        "paddingLeft":"350px"
        }
    )

if __name__ =="__main__":
    app.run()
    
#*********************PART 10****************************

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta",
             style ={ 
                 "paddingLeft":"350px"
                 }),
  ],
    style ={ 
        "backgroundColor":"GOld",
        "textAlign":"Left",
        "width":"800px",
        "display":"flex",   
        "paddingLeft":"350px"
        }
    )

if __name__ =="__main__":
    app.run()


#*********************PART 11 Line Graph****************************
# line graph
a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig =px.line(x =a,y=b)

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta",
             style ={ 
                 "paddingLeft":"350px",
                 # "display":"flex",   
                 }),
    html.Div(dcc.Graph(figure =fig),
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




#*********************PART 12 Line Graph****************************
# line graph
a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig =px.line(x =a,y=b,markers="marker+lines")

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta",
             style ={ 
                 "paddingLeft":"350px",
                 # "display":"flex",   
                 }),
    html.Div(dcc.Graph(figure =fig),
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




#*********************PART 13 Line Graph****************************
# line graph
a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig =px.line(x =a,y=b,markers="marker+lines",color=c)

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta",
             style ={ 
                 "paddingLeft":"350px",
                 # "display":"flex",   
                 }),
    html.Div(dcc.Graph(figure =fig),
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





#*********************PART 14 Line Graph****************************
# line graph
a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig =px.line(x =a,y=b,markers="marker+lines",color=c,hover_name=a)

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta",
             style ={ 
                 "paddingLeft":"350px",
                 # "display":"flex",   
                 }),
    html.Div(dcc.Graph(figure =fig),
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



#*********************PART 15 Line Graph****************************
# line graph
a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig =px.line(x =a,y=b,markers="marker+lines",color=c,hover_name=a,text=c)

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta",
             style ={ 
                 "paddingLeft":"350px",
                 # "display":"flex",   
                 }),
    html.Div(dcc.Graph(figure =fig),
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


#*********************PART 16 Line Graph****************************
# line graph
a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig =px.line(x =a,y=b,markers="marker+lines",color=c,hover_name=a,text=c,
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
    html.Div(dcc.Graph(figure =fig),
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



#*********************PART 17 Line Graph****************************
# line graph
a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig =px.line(x =a,y=b,markers="marker+lines",color=c,hover_name=a,text=c,
             color_discrete_sequence=["pink","orange","purple"],animation_frame=c)

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World"),
    html.Div("My Name is Taral Mehta",
             style ={ 
                 "paddingLeft":"350px",
                 # "display":"flex",   
                 }),
    html.Div(dcc.Graph(figure =fig),
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
    

#*********************PART 18 BAR Graph****************************
# line graph
a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig1 =px.bar(x =a,y=b,color=c,hover_name=a,text=c,
             color_discrete_sequence=["pink","orange","purple"],animation_frame=c)

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
    
   
#*********************PART 19 BAR Graph horizonatl****************************
# line graph
a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig1 =px.bar(x =a,y=b,color=c,hover_name=a,text=c,orientation="h",
             color_discrete_sequence=["pink","orange","purple"],animation_frame=c)

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
    

#*********************PART 19 Pie Graph****************************
# line graph
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
    
#*********************PART 20 Scatter Graph****************************
# line graph
a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig1 =px.scatter(x =b,y =b,color=c,hover_name=a,
             color_discrete_sequence=["pink","orange","purple"],animation_frame=c)

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
    
#*********************PART 21 Area Graph****************************
# line graph
a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig1 =px.area(x =b,y =b,color=c,hover_name=a)

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
    
   
#*********************PART 21 histogram Graph****************************
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
    
#*********************PART 22 histogram Graph****************************
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

    
#*********************PART 23 box Graph****************************
# line graph
a =["Ajay","Sumit","Raghu","Shreya","Parul"]
b =[40,32,33,44,25]
c =["Mumbai","Thane","Navi Mumbai","Thane","Mumbai"]

fig1 =px.box(x=c, y=b,color =c)

app =dash.Dash()

app.layout = html.Div(
    children=[
    html.Div("Hello World",
    style ={"display":"row"})],
  )
style ={ 
    "backgroundColor":"GOld",
    "textAlign":"Left",
    "width":"800px",
    # "paddingLeft":"350px"
    }
if __name__ =="__main__":
    app.run()



#***********************bootstrap********************************
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import dash_bootstrap_components as dbc
import datetime as dt
import pandas_datareader.data as web 


app =dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
fig1 =px.box(x=c, y=b,color =c)


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
        dbc.Col(dcc.Graph(id="linegraph0"),width ={'size':4}),
        dbc.Col(dcc.Graph(id="linegraph1"),width ={'size':4}),
        ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="linegraph2"),width ={'size':4}),
        dbc.Col(dcc.Graph(id="linegraph3"),width ={'size':4}),  
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
      ])  
  
if __name__ =="__main__":
    app.run()