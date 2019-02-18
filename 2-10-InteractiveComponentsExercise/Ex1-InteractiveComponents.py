#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:


app.layout = html.Div([
    dcc.RangeSlider(
        id='slider',
        marks={i: '{}'.format(i) for i in range(-10, 11)},
        min=-10,
        max=10,
        value=[-1, 1]
    ), 
    html.H1( id='number')
], style={'fontFamily':'helvetica', 'fontSize':50})

# Create a Dash callback:
@app.callback(
    Output(component_id='number', component_property='children'),
    [Input(component_id='slider', component_property='value')])
def update_multipled_number(value):
    return value[0]*value[1]


# Add the server clause:
if __name__ == '__main__':
    app.run_server()