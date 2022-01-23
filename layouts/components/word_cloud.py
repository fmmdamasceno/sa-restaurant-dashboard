from dash import html
from dash import dcc


layout = html.Div([
    html.Div(
        [
            html.Div(['Nuvem de Palavras'], className='menu-title'),
            html.Div(
                dcc.Graph(
                    id="restaurant-wordcloud",
                    config={"displayModeBar": False},
                ),
                className="card",
            ),
        ],
        className="wrapper",
    ),
])