from dash import html
from dash import dcc
from layouts.components import (
    header,
    exploration
)

layout = html.Div([
    header.layout,
    exploration.layout,
])