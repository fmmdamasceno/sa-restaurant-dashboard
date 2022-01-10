from dash import html, dcc
import numpy as np
from layouts import header
from utils import data

layout = html.Div([
    header.layout,
    html.Div([
        html.Div([
            html.Div('Restaurante', className="menu-title"),
            dcc.Dropdown(
                id='restaurant-filter-compare',
                options=[
                    {'label': restaurant, 'value': restaurant}
                    for restaurant in np.sort(data.restaurante.unique())
                ],
                multi=True,
                value=[],
                clearable=False,
                className="dropdown",
            )
        ]),
        html.Div([
            html.Div('Idioma', className="menu-title"),
            dcc.Dropdown(
                id='language-filter-compare',
                options=[
                    {'label': language, 'value': language}
                    for language in np.sort(data.idioma.fillna('Any').unique())
                ],
                value='Any',
                clearable=False,
                className="dropdown",
            )
        ]),
        html.Div([
            html.Div(
                children="Período",
                className="menu-title"
                ),
            dcc.DatePickerRange(
                id="date-range-compare",
                min_date_allowed=data.data.min().date(),
                max_date_allowed=data.data.max().date(),
                start_date=data.data.min().date(),
                end_date=data.data.max().date(),
            ),
        ]),
    ],className="menu",
    ),
    html.Div(
        [
            html.Div(
                dcc.Graph(
                    id="restaurant-rating-compare",
                    config={"displayModeBar": False},
                ),
                className="card",
            ),
        ],
        className="wrapper",
    ),
])
