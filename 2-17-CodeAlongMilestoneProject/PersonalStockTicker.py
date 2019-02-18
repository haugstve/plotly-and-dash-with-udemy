## Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


## Initialize app

app = dash.Dash()

## Add graph layout
## Use div to make boxes where we know the information is going

app.layout = html.Div([
    html.Div(
        html.H1('Stock ticker dashboard'),
        style={'color':'blue', 'border':'2px blue solid', 'borderRadius':5, 'padding':10}
    ),
    html.Div([
        html.Div([
            html.Div(
                'Select stock symbols',
                style={'color':'black', 'border':'2px black solid', 'borderRadius':5,
                    'padding':0, }
            ),
            html.Div(
                'Search and add here',
                style={'color':'black', 'border':'2px black solid', 'borderRadius':5,
                    'padding':0, }
            )
        ], style={'color':'blue', 'border':'2px blue solid', 'borderRadius':5,
                   'padding':0, 'width':'30%', 'display':'inline-block'}
        ),
        html.Div([
            html.Div(
                'Select start and end dates',
                style={'color':'black', 'border':'2px black solid', 'borderRadius':5,
                    'padding':0, }
            ),
            html.Div(
                'Date picker goes here',
                style={'color':'black', 'border':'2px black solid', 'borderRadius':5,
                    'padding':0, }
            )
        ], style={'color':'blue', 'border':'2px blue solid', 'borderRadius':5,
                   'padding':0, 'width':'30%', 'display':'inline-block'}
        ),
        html.Div([
            html.Div(
                '',
                style={'color':'black', 'border':'2px black solid', 'borderRadius':5,
                    'padding':0, }
            ),
            html.Div(
                'Button in this one',
                style={'color':'black', 'border':'2px black solid', 'borderRadius':5,
                    'padding':0, }
            )
        ], style={'color':'blue', 'border':'2px blue solid', 'borderRadius':5,
                   'padding':0, 'display':'inline-block'}
        )
    ], style={'color':'red', 'border':'2px red solid', 'borderRadius':5,
              'padding':10, 'width':'80%'}),
    html.Div(
        'Graph goes here',
        style={'color':'green', 'border':'2px green solid', 'borderRadius':5,
           'padding':10, 'width':'80%'}
    )
])

## Start the server
if __name__ == "__main__":
    app.run_server()