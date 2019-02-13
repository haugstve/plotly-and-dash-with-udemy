#######
# Objective: Create a scatterplot of 1000 random data points.
# x-axis values should come from a normal distribution using
# np.random.randn(1000)
# y-axis values should come from a uniform distribution over [0,1) using
# np.random.rand(1000)
######

# Perform imports here:
import numpy as np
import pandas as pd
import plotly.offline as pyo 
import plotly.graph_objs as go


x = np.random.randint(1,101,100)
y = np.random.randint(1,101,100)

# Define a data variable
data = [go.Scatter(
    x=x, 
    y=y, 
    mode='markers',
    marker={
        'size': '20', 
        'symbol': 'pentagon',
        'color': 'rgb(0,0,0)'
    }
)]


# Define the layout
layout = go.Layout(title="Test scatter plot",
                   xaxis={'title': 'Some x'},
                   yaxis={'title': 'another y'},
                   hovermode ='closest')


# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='tmp.html')