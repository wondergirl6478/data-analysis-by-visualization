import pandas as pd     
import statistics
import plotly.express as px
import csv 

df = pd.read_csv(r"/Users/muraliganguri/Downloads/class 107 project/data.csv")
print(df.groupby("level")["attempt"].mean())
fig = px.scatter(df,x = df.groupby("level")["attempt"].mean(), y = ['Level 1','Level 2','Level 3','Level 4'], color = 'level' )
fig.show()