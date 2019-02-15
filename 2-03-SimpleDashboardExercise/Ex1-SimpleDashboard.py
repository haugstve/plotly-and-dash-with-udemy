#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go 
# import plotly.offline as pyo
import pandas as pd

# Launch the application:
app = dash.Dash()

# Colors
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# Create a DataFrame from the .csv file:
df = pd.read_csv('../Data/OldFaithful.csv')

# Create a Dash layout that contains a Graph component:
data = [go.Scatter(x=df['X'],y=df['Y'],mode='markers')]
layout = go.Layout(
    title = 'Old Faithful', 
    plot_bgcolor = colors['background'],
    paper_bgcolor = colors['background'],
    font = {'color': colors['text']}
    )

fig = go.Figure(data = data, layout = layout)

app.layout = html.Div(
    children=[
        html.H1(
            children='Hello Dash', 
            style={'textAlign': 'center', 'color': colors['text']}
            ),
        html.Div(
            children='Dash: A web application framework for Python.', 
            style={'textAlign': 'center', 'color': colors['text']}
            ),
        dcc.Graph(id='example-graph', figure = fig)
        ],
    style={'backgroundColor': colors['background']}
    )

# Add the server clause:
if __name__ == '__main__':
    app.run_server()