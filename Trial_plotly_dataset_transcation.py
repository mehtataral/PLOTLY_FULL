# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 17:55:55 2022

@author: user
"""
import pandas as pd 
import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output


df = pd.read_csv(r"C:\Users\user\Desktop\Plotly\Dataset\transactions.csv",parse_dates=["date"])
df
df.info()
df.isnull().sum()
unique_category = df.category.unique()
unique_category 


df['year'] = pd.to_datetime(df['date']).dt.to_period('Y')#it provides month and year together
df.info()
df['month'] = pd.to_datetime(df['date']).dt.month#it provides month and year together
df.info()
df['month_year'] = pd.to_datetime(df['date']).dt.to_period('Y')#it provides month and year together
df.info()

#*********************groceries*****************
groceries_table = df.loc[df.category =="groceries"]
groceries_table.info()
groceries_table
groceries_table.amount.min()
groceries_table.amount.max()

groceries_table.set_index("date",inplace =True)
# groceries_table.reset_index(inplace =True)
groceries_table

# groceries_table['year'] = pd.DatetimeIndex(groceries_table['date']).year
# groceries_table.head()


# groceries_table['month'] = pd.DatetimeIndex(groceries_table['date']).month
# groceries_table.head()


groceries_table.resample("M").sum() # for finding number of years

groceries_table.date.dt.year 
groceries_table.date.dt.month 

groceries_table['year'] = groceries_table['date'].dt.year
groceries_table.year.unique()

groceries_table['month'] = groceries_table['date'].dt.month
groceries_table.month.unique()

# groceries_table['year'] = pd.to_datetime(groceries_table['year'])
# groceries_table.drop("year",inplace =True,axis= "columns")

groceries_table.loc[groceries_table["year"]==2020].amount.min()
groceries_table.loc[groceries_table["year"]==2020].amount.max()
groceries_table.loc["2020"].amount.min()
groceries_table.loc["2020"].amount.max()

groceries_table.loc["2021"].amount.min()
groceries_table.loc["2021"].amount.max()

groceries_table.loc["2022"].amount.min()
groceries_table.loc["2022"].amount.max()



groceries_table.loc[(groceries_table["year"]==2020)&(groceries_table["month"]==5)].amount.min()
groceries_table.loc[(groceries_table["year"]==2020)&(groceries_table["month"]==5)].amount.max()



# fig10 =px.bar(groceries_table,groceries_table.year,groceries_table.amount)
# fig10 =px.bar(groceries_table,groceries_table.date,groceries_table.amount,color ="year")
# fig11 =px.pie(groceries_table,groceries_table.date)
# fig11 =px.line(groceries_table,groceries_table.date,groceries_table.amount,color ="year")

 
#*********************entertainment*****************
entertainment_table = df.loc[df.category =="entertainment"]
entertainment_table
entertainment_table.amount.min()
entertainment_table.amount.max()

#*********************healthcare*****************
healthcare_table = df.loc[df.category =="healthcare"]
healthcare_table
healthcare_table.amount.min()
healthcare_table.amount.max()

#*********************utilities*****************
utilities_table = df.loc[df.category =="utilities"]
utilities_table
utilities_table.amount.min()
utilities_table.amount.max()

#*********************car*****************
car_table = df.loc[df.category =="car"]
car_table
car_table.amount.min()
car_table.amount.max()

#*********************housing*****************
housing_table = df.loc[df.category =="housing"]
housing_table
housing_table.amount.min()
housing_table.amount.max()

#*********************travel*****************
travel_table = df.loc[df.category =="travel"]
travel_table
travel_table.amount.min()
travel_table.amount.max()
import numpy as np

df1 =df.copy()
df
df1
# df1.set_index("date",inplace =True)
x1= df1.loc["2022"]
x1
df1["2020"]
df1["2021"]
df1["2022"]

x1 = df1.resample("m").sum()
x1
app =dash.Dash()
type(app)

# fig =px.line(df,x ="category",y ="amount",color ="category")
# fig =px.line(df,y ="category",x ="amount",color ="category")
# fig =px.scatter(df,y ="category",x ="amount",color ="category")
# 
# fig1 =px.line(x1,x1.index,x1["amount"])
# fig2 =px.line(travel_table,travel_table.date,travel_table["amount"],color ="category")
# fig3 =px.line(housing_table,housing_table.date,housing_table["amount"],color ="category")
# fig4 =px.line(car_table,car_table.date,car_table["amount"],color ="category")
# fig5 =px.line(utilities_table,utilities_table.date,utilities_table["amount"],color ="category")
# fig6 =px.line(healthcare_table,healthcare_table.date,healthcare_table["amount"],color ="category")
# fig6 =px.line(df,df.index,df["amount"],color ="category")
# fig7 =px.bar(df,df.index,df["amount"],color ="category")
# fig8 =px.scatter(df,df.index,df["amount"],color ="category")

# fig6 =px.line(df1,df.amount,df1.index ,color =df["category"])
# fig7 =px.bar(df,df.amount,df["date"],color =df.category,barmode="stack")
# fig8 =px.scatter(df,df.date,df["amount"],color=df.category,animation_frame="category",size ="amount")
# fig9 =px.pie(df,df.category,color_discrete_sequence=["pink","cyan","orange","lightblue","purple","maroon","lightgreen"])

app.layout = html.Div( style ={ 
    "backgroundColor":"#111111"
    },
    children =[
        
        html.Div("First Graph"), 
        dcc.Dropdown(id ="dropdown",
                     style ={
                         "backgroundColor":"Pink",
                         "textAlign":"Center",
                         "color":"Green",
                         },
            options = [
                {
                    'label':"month_year",
                    'value':"month_year"
                },
                {
                    "label":"category",
                    'value':"category"
                },
                # {
                #     'label':"date",
                #     'value':"date"
                # },
                # {
                #     'label':"year",
                #     'value':"year"
                # },
                # {
                #     'label':"month",
                #     'value':"month"
                # },
                # {
                #     'label':"housing",
                #     'value':"housing"
                # },{
                #     'label':"travel",
                #     'value':"travel"
                # }
                ],
                # value = "date",
           ),
      #   dcc.Graph(id ="linegraph",
      #             figure =fig1),
      #   dcc.Graph(id ="linegraph1",
      #             figure =fig6,),
      #   dcc.Graph(id ="linegraph2",
      #             figure =fig7,),

      # dcc.Graph(id ="linegraph3",
      #           figure =fig8,),
      # dcc.Graph(id ="linegraph4",
      #           figure =fig9,),
      # dcc.Graph(id ="linegraph5",
      #     figure =fig,),
       dcc.Graph(id ="linegraph6",
               # figure =fig,
               ),
        ]
    
    )

@app.callback(Output(component_id="linegraph6",component_property="figure"),
              [Input(component_id="dropdown",component_property="value")]
  
)
def A(drop):
    fig =px.scatter(df,y =drop,x ="amount")
    return fig
    

if __name__ =="__main__":
    app.run()
















