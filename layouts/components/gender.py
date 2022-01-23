from dash import html
from dash import dcc


layout = html.Div([
    html.Div(
        [
            html.Div(['Distribuição por Gênero'], className='menu-title'),
            html.Div(
                dcc.Graph(
                    id="gender-distribution",
                    config={"displayModeBar": False},
                ),
                className="card",
            ),
        ],
        className="wrapper",
    ),
])