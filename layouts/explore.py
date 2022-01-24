from dash import html
from dash import dcc
from layouts.components import (
    menu,
    header,
    footer,
    exploration
)

layout = html.Div([
    menu.layout,
    header.layout,
    exploration.layout,
    footer.layout
])