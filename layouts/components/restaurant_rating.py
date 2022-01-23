from dash import html
from dash import dcc



layout = html.Div([
    html.Div(
        [
            html.Div(['Avaliação Média'], className='menu-title'),
            html.Div(
                dcc.Graph(
                    id="restaurant-rating",
                    config={"displayModeBar": False},
                ),
                className="card",
            ),
        ],
        className="wrapper",
    ),
])