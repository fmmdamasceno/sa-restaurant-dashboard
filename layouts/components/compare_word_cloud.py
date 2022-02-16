from dash import html
from dash import dcc



layout = html.Div([
    html.Div([
        html.Div([
            html.H5(['Nuvem de palavras'], className='card-title'),
            dcc.Graph(
                id="restaurant-wordcloud-compare",
                config={
                    "displayModeBar": False,
                    "responsive": True
                },
                style={'height': '30vh'},
            )
        ],className="card-body p-1"),
    ],className="card",
    ),
],className='col-md-12')