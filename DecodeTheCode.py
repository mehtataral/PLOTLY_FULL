# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:08:58 2023

@author: user
"""
#Dash is open source library
#It is python framework for building analytical web application
#it is powerful library

#plotly develops dash 
# Dash apps are composed of two parts .
# 1. Layout
# 2. Callback

# It’s especially useful for Python data scientists who aren’t very familiar 
# with web development. Users can create amazing dashboards in their browser 
# using dash.

# Built on top of Plotly.js, React, and Flask, Dash ties modern UI elements 
# like dropdowns, sliders and graphs directly to your analytical python code.

#Dash HTML Component contain a components class for every HTML tags as well as
# keywords for all the HTML arguments

# Dash applications are written purely in python,so NO HTML or JavaScript 
# is necessary.

import pandas as pd
import numpy as np

import dash  #pip install dash 
import dash_core_components as dcc      #pip install dash_core_components
import dash_html_components as html     #pip install dash_html_components
import plotly.express as px             #pip install plotly.express

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
        # "width":"200px"
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
        "display":"row",   
        "paddingLeft":"350px"
        }
    )

if __name__ =="__main__":
 b     app.run()

#*********************PART 11****************************

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
    
