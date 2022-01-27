from dash import html
from dash import dcc


layout = html.Div([
    html.Div([
        html.Div([
            html.H5(['Distribuição da avaliação por plataforma'], className='card-title'),
            dcc.Graph(
                id="rating-by-platform",
                config={"displayModeBar": False},
                style={'height': '34vh'}
            ),
        ],className="card-body p-1"),
    ],className="card"),
],className='col-md-4')