#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset (../data/abalone.csv).
# Set the range from 0 to 1, with a bin size of 0.02
######

# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo


# create a DataFrame from the .csv file:
df = pd.read_csv('../data/abalone.csv')

# create a data variable:
data = [go.Histogram(x=df['length'], xbins={'start':'0','end':'1','size':'0.02'})]


# add a layout
layout = go.Layout(title='Shell length from the abalone dataset')

# create a fig from data & layout, and plot the fig
fig = go.Figure(layout=layout, data=data)
pyo.plot(fig)