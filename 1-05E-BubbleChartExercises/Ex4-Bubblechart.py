#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/mpg.csv')

# create data by choosing fields for x, y and marker size attributes
data = [go.Scatter(x=df['acceleration'], y=df['mpg'],
                    mode='markers', marker={'size': df['displacement']/10, 'color':df['cylinders']})]


# create a layout with a title and axis labels
layout = go.Layout(title='Car Performance', 
                    xaxis={'title':'Acceleration'},
                    yaxis={'title':'Miles per gallon'})


# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)