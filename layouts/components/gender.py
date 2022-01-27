from dash import html
from dash import dcc



layout = html.Div([
    html.Div([
        html.Div([
            html.H5(['Reviews por Gênero'], className='card-title'),
            dcc.Graph(
                id="gender-distribution",
                config={"displayModeBar": False},
                style={'height': '30vh'}
            )
        ],className="card-body p-1"),
    ],className="card",
    ),
],className='col-md-4')