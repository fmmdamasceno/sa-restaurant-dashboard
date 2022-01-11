from dash import html, dcc
import numpy as np
import pandas as pd
import random
from layouts import header
import utils

data = utils.load_dataset()

layout = html.Div([
    header.layout,
    html.Div([
        html.Div([
            html.Div('Restaurante', className="menu-title"),
            dcc.Dropdown(
                id='restaurant-filter',
                options=[
                    {'label': restaurant, 'value': restaurant}
                    for restaurant in np.sort(data.restaurante.unique())
                ],
                value=random.choice([r for r in np.sort(data.restaurante.unique())]),
                clearable=False,
                className="dropdown",
            )
        ]),
        html.Div([
            html.Div('Idioma', className="menu-title"),
            dcc.Dropdown(
                id='language-filter',
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
                id="date-range",
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
                    id="restaurant-rating",
                    config={"displayModeBar": False},
                ),
                className="card",
            ),
        ],
        className="wrapper",
    ),
    html.Div(
        [
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