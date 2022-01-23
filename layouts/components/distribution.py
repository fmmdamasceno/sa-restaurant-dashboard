from dash import html
from dash import dcc


layout = html.Div([
    html.Div([
        html.Div(['Distribuição dos comentários'], className='menu-title'),
        html.Div(
            dcc.Graph(
                id="comment-distribution",
                config={"displayModeBar": False},
            ),
            className="card",
        ),
    ],
    className="wrapper",
    ),
])