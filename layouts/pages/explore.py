from dash import html
from dash import dcc
from layouts.pages import menu, header, footer
from layouts.components import (
    exploration
)

layout = html.Div([
    menu.layout,
    header.layout,
    html.Div([
        html.H1("Explore os dados", style={'text-align':'center'})
    ]),
    exploration.layout,
    footer.layout
])