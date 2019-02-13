#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
import numpy as np

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/abalone.csv')

np.random.seed(42)

# take two random samples of different sizes:
sample_0 = np.random.choice(df['rings'],7,replace=False)
sample_1 = df['rings'][np.random.randint(0,len(df.index),9)]
sample_2 = df['rings'][np.random.randint(0,len(df.index),5)]

# create a data variable with two Box plots:
data = [go.Box(y=sample_1,name='A',boxpoints='all'), 
        go.Box(y=sample_2,name='B',boxpoints='all'), 
        go.Box(y=sample_0,name='C',boxpoints='all')]


# add a layout
layout = go.Layout(title='Compare distributions')

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)