#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('../data/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']


# Use a for loop (or list comprehension to create traces for the data list)
data = []

for day in days:
    # What should go inside this Scatter call?
    df_day = df[df.DAY == day]
    trace = go.Scatter(x=df_day.LST_TIME, y=df_day.T_HR_AVG, mode='lines')
    data.append(trace)

data2 = [go.Scatter(x=df['LST_TIME'], y=df[df['DAY']==day]['T_HR_AVG'], mode='lines', name=day) for day in days]

# Define the layout
layout = go.Layout(xaxis={'title':'Hour'},yaxis={'title':'Temp'})


# Create a fig from data and layout, and plot the fig
pyo.plot(data2,layout)