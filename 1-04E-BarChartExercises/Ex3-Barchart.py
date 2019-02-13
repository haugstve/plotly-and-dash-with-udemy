#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/mocksurvey.csv',index_col=0)

# create traces using a list comprehension:
traces = [go.Bar(x=df.index, y=df[opinion], name=opinion) for opinion in df.columns]

# This only works if you have 
#traces2 = [go.Bar(y=df['Unnamed: 0'], x=df[opinion], name=opinion, orientation='h') for opinion in df.columns[1:]]

# create a layout, remember to set the barmode here
layout = go.Layout(barmode='stack')

# create a fig from data & layout, and plot the fig.
fig = go.Figure(data=traces,layout=layout)
pyo.plot(fig)