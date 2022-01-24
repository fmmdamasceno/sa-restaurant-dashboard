from dash import html
from dash import dcc



layout = html.Div([
    html.Div(
        [
            html.Div(['Classificação dos Reviews'], className='menu-title'),
            html.Div(
                dcc.Graph(
                    id="review-classification",
                    config={"displayModeBar": False},
                ),
                className="card",
            ),
        ],
        className="wrapper",
    ),
])