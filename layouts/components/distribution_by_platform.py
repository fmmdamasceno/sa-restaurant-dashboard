from dash import html
from dash import dcc


layout = html.Div([
    html.Div([
        html.Div([
            html.H5(['Distribuição da avaliação por plataforma'], className='card-title'),
            dcc.Graph(
                id="rating-by-platform",
                config={"displayModeBar": False},
            ),
        ],className="card-body p-1"),
    ],className="card"),
],className='col-md-4')