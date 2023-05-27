# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:28:24 2023

@author: user
"""

name = "Taral Mehta"
print(name)
course ="DSP"
course
roll = 55


#pandas 
#pip install pandas


import pandas as pd

emp = {"Name":["Mohit","Rohit","Shobhit","Ram","Shyam","Ramesh","Suresh"],
       "Age":[22,66,44,77,60,10,55],
       "city":["Mumbai","Thane","Thane","Mumbai","Navi Mumbai","Thane","Mumbai"]
       }
df =pd.DataFrame(emp) #Table created
print(df)

#iloc  and loc
#integer location
#location
# df.iloc[row,col]
df.iloc[0:3,0:3]
df.iloc[0:3,:] 
df.iloc[0:3,-1]
df.iloc[:,0:-1]


      Name  Age         city
0    Mohit   22       Mumbai
1    Rohit   66        Thane
2  Shobhit   44        Thane
3      Ram   77       Mumbai
4    Shyam   60  Navi Mumbai
5   Ramesh   10        Thane
6   Suresh   55       Mumbai

Task1
# 5   Ramesh   10        Thane

Task2
# 2  Shobhit   44        Thane
# 3      Ram   77       Mumbai
# 4    Shyam   60  Navi Mumbai

Task3
# 3      Ram   77
# 4    Shyam   60

Task4
# 4   60        Navi Mumbai
# 5   10        Thane




