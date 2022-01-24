from dash import html
from dash import dcc



layout = html.Div([
    html.Div(
        [
            html.Div(['Top reviewers'], className='menu-title'),
            html.Div(
                dcc.Graph(
                    id="top-reviewers",
                    config={"displayModeBar": False},
                ),
                className="card",
            ),
        ],
        className="wrapper",
    ),
])