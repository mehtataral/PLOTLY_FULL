# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:26:53 2022

@author: user
"""
import pandas as pd 
import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output

df = pd.read_csv(r"https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv",parse_dates=["Date"])
df
df.info()
df.isnull().sum()  
df1_copy = df.copy() 
df1_copy
df1_copy.set_index("Date",inplace = True) # if index is true then we can't get DATE COLUMN 
x1 = df.iloc[:,:-1]
# df1 = px.data.stocks(indexed=True)-1
fig1 = px.line(df, x=df.Date, y="AAPL.Open")
fig2 = px.bar(df, x=df.Date, y="AAPL.Open")
fig3 = px.area(df1_copy, facet_col="direction", facet_col_wrap=2)
fig4 = px.line(x1,x=x1.Date,y=x1.columns, hover_name= "AAPL.Low",
               hover_data= ["AAPL.Open","AAPL.Close"],#hover_data=dict(x1.index: "|%B %d, %Y"),
              title='custom tick labels')

df1 =df.loc[df.Date >= "2016-11-21"]
fig5 = px.line(df1, x ="Date",y ="AAPL.Open")
fig5.update_xaxes(rangeslider_visible=True)
  

df2 = df.loc[(df["Date"] >= "2015-04-30") & (df["Date"] <= "2016-12-22")]
df2.drop("direction",inplace=True,axis ="columns")
fig6 = px.line(df2, x ="Date",y =df2.columns)
fig6.update_xaxes(rangeslider_visible=True)


fig7 = px.line(df, x='Date', y='AAPL.High', range_x=['2016-07-01','2016-10-31'])#range ofdate   
fig7.update_xaxes(rangeslider_visible=True)
 

# histfunc =  ['count', 'sum', 'avg', 'min', 'max']
fig8 = px.histogram(df, x="Date", y="AAPL.Close", histfunc="sum", title="Histogram on Date Axes")
# fig2 = px.line(df, x='Date', y="AAPL.Open",color ="direction")
# fig3 = px.line(df, x='Date', y="AAPL.Open",color ="direction")
fig9 = px.line(df, x="Date", y="AAPL.Close", title="Histogram on Date Axes")
fig9.update_xaxes(rangeslider_visible =True,
                  rangeselector =dict(
                      buttons =list([
                          # step =['month', 'year', 'day', 'hour', 'minute', 'second','all']
                          # stepmode =['backward', 'todate']
                          dict(count=1,label ="1Month",step="month",stepmode ="backward"),
                          dict(count=6,label ="6M",step="month",stepmode ="backward"),
                          dict(count=1,label ="YTD",step="year",stepmode ="todate"),
                          dict(count=1,label ="1Y",step="year",stepmode ="backward"),
                          dict(step ="all")
                          ])
                      )
                  )   

app =dash.Dash()

app.layout = html.Div( style ={ 
    "backgroundColor":"#111111"
    },
    children =[
        dcc.Dropdown(id ="dropdown",
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
               "value":"AAPL.Close"
               }], clearable=False,
            ),
        html.Div("First Graph"), 
        dcc.RadioItems(['Increasing', 'Decreasing'], 'Increasing', id="gender"),
        dcc.Graph(id ="temp"),
        
        dcc.Graph(id ="linegraph1",
          figure =fig1,),
        dcc.Graph(id ="linegraph2",
           figure =fig2,
          ),
        dcc.Graph(id ="linegraph3",
           figure =fig3,    
          ),
        dcc.Graph(id ="linegraph4",
           figure =fig4,    
          ),
        dcc.Graph(id ="linegraph5",
           figure =fig5,    
          ),
        dcc.Graph(id ="linegraph6",
           figure =fig6,    
          ),
        dcc.Graph(id ="linegraph7",
           figure =fig7,    
          ),
        dcc.Graph(id ="linegraph8",
           figure =fig8,    
          ),
        dcc.Graph(id ="linegraph9",
           figure =fig9,    
          ),
        dcc.Graph(id ="linegraph",
          ),
        ]
    )
@app.callback(
    Output("linegraph", "figure"), 
    Input("dropdown", "value"))


def display_time_series(dropdown):
  print(dropdown)              

  # if dropdown is None:
  #   return
  # df = pd.read_csv(r"https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv",parse_dates=["Date"])
  # df = px.data.stocks() # replace with your own data source
  # fig = px.line(df, x='Date', y=dropdown)
  fig = px.line(df, x=df.index, y=dropdown)
  return fig

@app.callback(Output("temp", "figure"), Input("gender", "value"))
def gender_change(value):
  print("=============")
  print(value)
  df_filterd = df[df["direction"] == value]
  print(df_filterd)
  fig = px.line(df_filterd, x=df_filterd["Date"], y=df_filterd["AAPL.Close"])  
  return fig

 
if __name__ =="__main__":
    app.run(debug=True)

