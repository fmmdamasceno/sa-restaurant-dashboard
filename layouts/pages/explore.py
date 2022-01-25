from dash import html
from dash import dcc
from layouts.pages import menu, header, footer
from layouts.components import (
    exploration
)

layout = html.Div([
    menu.layout,
    header.layout,
    exploration.layout,
    footer.layout
])