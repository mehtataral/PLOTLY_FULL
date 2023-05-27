# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 13:36:42 2022

@author: user
"""
a =bool(input("enter"))
a
import pandas as pd 
import numpy as np
import plotly.graph_objs as graph
import plotly.offline as offline


df = pd.read_csv(r"C:\Users\user\Desktop\CARDS\Project\Data science\Placement_Data_Full_class.csv")
df
df.info()
df.isnull().sum()
df.salary.fillna(0,inplace =True)
df.isnull().sum()
df["salary"]=df["salary"].astype(int)
df

df.drop("sl_no",axis ="columns",inplace =True)
df.specialisation.unique()
#*************** Gender = Male and Female  *******************
only_Male = df.loc[df["gender"] == "M"]
only_Male

only_FMale = df.loc[df["gender"] == "F"]
only_FMale
#*************** workexp  yes  / no *******************
wrk_yes = df.loc[df["workex"] == "Yes"]
wrk_yes

wrk_no = df.loc[df["workex"] == "No"]
wrk_no
#*************** Mkt&HR &  Mkt&Fin  *******************
specialisation_fin = df.loc[df["specialisation"] == "Mkt&Fin"]
specialisation_fin


specialisation_HR = df.loc[df["specialisation"] == "Mkt&HR"]
specialisation_HR

# category_sales=data.groupby('SubCategory').sum().reset_index()
# plot = go.Figure(data=[go.Bar(name='Sales',x=category_sales['SubCategory'],y=category_sales['Sales']
# ),
#     go.Bar(name='Discount',x=category_sales['SubCategory'],y=category_sales['Discount']
# ),
#     go.Bar(name='Shipping',x=category_sales['SubCategory'],y=category_sales['Shipping']
# )
# ])
# Add dropdown
# plot.update_layout(
#     updatemenus=[
#         dict(
#             active=0,
#             buttons=list([
#                 dict(label="Sales",method="update",args=[{"visible": [False, False, True]},
#                            {"title": "Sales"}]),
#                 dict(label="Discount",method="update",args=[{"visible": [False,True, False]},
#                            {"title": "Discounts",
#                             }]),
#                 dict(label="Shipping",method="update",args=[{"visible": [True, False, False]},
#                            {"title": "Shipping Costs",
#                             }]),
#             ]),
#         )
#     ])
 
# plot.show()
#************************ Groupby merge data**********************
x1 =df.groupby(["gender"]).sum().reset_index()
x1
x =df.groupby(["gender"]).count().reset_index()

x =df.groupby(["gender","status","workex"])["status"].count()
x
x =df.groupby(["gender","status"])["status"].count().plot(kind ="bar")
x
x =df.groupby(["gender","status","workex"])["status"].count().unstack(0).reset_index()
x.reset_index()
# x =df.groupby(["gender","status"])["status"].count().mean()
# x
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash()
fig1 = px.bar(df,df.gender,df.ssc_p, height=700,width=500,color ="workex",barmode ="group",
              color_discrete_sequence=["gold","silver"])
# fig1.update_layout({
# 'plot_bgcolor': 'rgba(250, 250, 250, 250)',
# 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
# })
# fig1 = px.bar(name='gender',x=x1['salary'],y=x1['workex'],barmode ="group",
#               color_discrete_sequence=["gold","silver"])
# fig1.update_layout(
#     updatemenus=[
#         dict(
#             active=0,
#             buttons=list([
#                 dict(label="Salary",method="update",args=[{"visible": [False, False, True]},
#                             {"title": "salry"}]),
#                 dict(label="status",method="update",args=[{"visible": [False,True, False]},
#                             {"title": "status",
#                             }]),
#                 dict(label="degree_p",method="update",args=[{"visible": [True, False, False]},
#                             {"title": "degree percentage",
#                             }]),
#             ]),
#         )
#     ])

fig2 = px.bar(df,df.workex,df.salary, height=700,width=500,color ="gender",barmode ="stack",
                  color_discrete_sequence=["lightpink","wheat"],hover_name='status')



fig3 = px.pie(df,df.status, height=700,width=500, 
              color_discrete_sequence=["Lightblue","firebrick"],hover_name='gender')


fig4 = px.scatter(df,df.salary,df["specialisation"], height=700,width=1000,color ="gender" ,
              color_discrete_sequence=["steelblue","purple"],
              hover_name='status',
               animation_frame='salary',
              )

df.salary.min()
df.salary.max()

fig5 = px.pie(df,df.gender, height=700,width=500 , #names =df.gender.unique(),
              color_discrete_sequence=["Grey","Lightblue"],hover_name='workex')


fig6 = px.pie(df,df.degree_t, height=700,width=500 ,#names =df.degree_t.unique(),
              color_discrete_sequence=["steelblue","thistle"],hover_name='mba_p')

fig7 = px.pie(df,df.specialisation, height=700,width=500 ,#names =df.specialisation.unique(),
              color_discrete_sequence=["steelblue","thistle"],hover_name='status')

    
fig8 = px.bar(df,df.salary,df.workex, height=700,width=500 ,orientation ="h",#names =df.specialisation.unique(),
              color_discrete_sequence=["steelblue","thistle"],hover_name='gender')  

app.layout = html.Div(
    
    style ={
        "backgroundColor" :"#111111",
        "fontColor":"pink",
        
        },
    
    children =[
    html.Label("DropDown List",
               style ={
                   "backgroundColor" :"grey",
                   "font_color":"RED",
                   },
               
               ),
    html.Br(),# BReak Line
    dcc.Dropdown(id ="dropdwn",options =[
        {"label":"Mkt&HR",
         "value":"Mkt&HR"            
            },     
        {"label":"Mkt&Fin",
         "value":"Mkt&Fin"            
            }],
        style ={
                "backgroundColor" :"white",
                "fontColor":"RED",
                }
        ),
    dcc.Dropdown(id ="dropdwn1",options =[
        {"label":"Sci&Tech",
         "value":"Sci&Tech"            
            },     
        {"label":"Comm&Mgmt",
         "value":"Comm&Mgmt"            
            },
        
        {"label":"Others",
         "value":"Others"            
            },
        ],
        style ={
                "backgroundColor" :"white",
                "fontColor":"RED",
                }
        ),
    html.Br(),# BReak Line
    html.Br(),# BReak Line
    html.Label("Range of Percentage",
               style ={
                   "backgroundColor" :"Grey",
                   "fontColor":"RED",
                   }),
    html.Br(),# BReak Line
    dcc.Slider(min =0,max =100,step=10,value=50,marks={i: "{}".format(i)for i in range(0,21,5)}),
    # dcc.Slider(
    #     min = 0,
    #     max =100,
    #     value = 40,
    #     marks = [10,20]
    #     ),
    html.Br(),# BReak Line
    html.Br(),# BReak Line
    html.Label("Gender : -",
               style ={
                   "backgroundColor" :"Grey",
                   "fontColor":"RED",
                   }),
    html.Br(),# BReak Line
    dcc.RadioItems(id ="radiobtn",
                   options =[
     {"label":"Male",
      "value":"Male"            
         },
     {"label":"Female",
      "value":"Female"            
         },
    ],
        style ={
        "backgroundColor" :"Grey",
        "fontColor":"pink",
        },    
        value ="Male"
        ),
    html.Br(),# BReak Line
   
    dcc.Graph(id ="frist Bar graph",
              figure = fig1),
    dcc.Graph(id ="2ndGraph",
              figure =fig2),
    dcc.Graph(id ="3rdGraph",
              figure =fig3),
    html.Div([
    dcc.Graph(id ="4thGraph",
              figure =fig4),
    dcc.Slider(id ="slider2",min =0,max =100000,step=None,value=None),
    ]),
    dcc.Graph(id ="5thGraph",
              figure =fig5),
    dcc.Graph(id ="6thGraph",
              figure =fig6),
    dcc.Graph(id ="7thGraph",
              figure =fig7),
    dcc.Graph(id ="8thGraph",
              figure =fig8),
    html.Div(id ="specialization"),
    
    ]) 

# @app.callback(
#               Output(component_id="4thGraph", component_property="figure"),
#               [Input(component_id="slider2", component_property="value")]
#               )
   
# def update_method(selected_salary):
#     filtered_df = df[df.salary == selected_salary]
    
#     fig4 = px.scatter(filtered_df,x ="salary",y ="specialisation", height=400,width=600,color ="gender" ,
#                   color_discrete_sequence=["steelblue","purple"],
#                   hover_name='status',
#                    # animation_frame='salary',
#                   )

#     fig4.update_layout(transition_duration=500)

#     return fig4


# def update_method(value):
#    filtered_df = df[df["workex"] == value]
#    if filtered_df == "Mkt&HR":
#         # fig2 = px.bar(df,df.workex,df.salary, height=700,width=500,color ="gender",barmode ="group")
#         return fig1 
#    elif filtered_df == "Mkt&Fin":
#          # fig2 = px.bar(df,df.workex,df.salary, height=700,width=500,color ="gender",barmode ="group")
#         return fig1

    
if __name__ == "__main__":
    app.run()

# help(dash.dcc.RadioItems)
