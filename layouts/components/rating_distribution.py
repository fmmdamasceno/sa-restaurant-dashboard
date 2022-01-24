from dash import html
from dash import dcc



layout = html.Div([
    html.Div(
        [
            html.Div(['Distribuição do rating'], className='menu-title'),
            html.Div(
                dcc.Graph(
                    id="rating-distribution",
                    config={"displayModeBar": False},
                ),
                className="card",
            ),
        ],
        className="wrapper",
    ),
])