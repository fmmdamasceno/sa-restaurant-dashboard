from dash import html
from dash import dcc



layout = html.Div([
    html.Div([
        html.Div([
            html.H5(['Quantidade de caracteres'], className='card-title'),
            dcc.Graph(
                id="character-count",
                config={"displayModeBar": False},
            ),
        ],className="card-body p-1"),
    ],className="card"),
],className='col-md-4')