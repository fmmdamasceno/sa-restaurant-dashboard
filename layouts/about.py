from dash import html
from dash import dcc
from layouts import menu, header, footer



layout = html.Div([
    menu.layout,
    header.layout,
    html.Div([
        html.P("Sobre...")
    ], className='container'),
    footer.layout
])