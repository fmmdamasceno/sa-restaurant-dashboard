from dash import html
from dash import dcc


layout = html.Div([
    html.Div([
        html.Div([
            html.H5(['Distribuição dos comentários'], className='card-title'),
            dcc.Graph(
                id="comment-distribution",
                config={"displayModeBar": False},
            ),
        ],className="card-body p-1"),
    ],className="card"),
],className='col-md-12')