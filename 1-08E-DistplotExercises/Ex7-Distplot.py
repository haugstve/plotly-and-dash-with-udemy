#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff
import scipy

# create a DataFrame from the .csv file:
df = pd.read_csv('../data/iris.csv')

# Define the traces
hist_data = [df[df['class']=='Iris-setosa']['petal_length'],
                df[df['class']=='Iris-virginica']['petal_length'],
                df[df['class']=='Iris-versicolor']['petal_length']]

group_labels = ['Iris-setosa','Iris-virginica','Iris-versicolor']
# HINT:
# This grabs the petal_length column for a particular flower
#df[df['class']=='Iris-some-flower-class']['petal_length']


# Define a data variable
data = ff.create_distplot(hist_data,group_labels,bin_size=[.2,0.4,0.4])

# Create a fig from data and layout, and plot the fig
pyo.plot(data)