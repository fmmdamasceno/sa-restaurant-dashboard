from dash import html
from dash import dcc
from layouts import header
from utils import (
    options_restaurants,
    options_idioms,
    option_random_restaurant,
    min_date,
    max_date
)

layout = html.Div([
    header.layout,
    html.Div([
        html.Div([
            html.Div('Restaurante', className="menu-title"),
            dcc.Dropdown(
                id='restaurant-filter',
                options=options_restaurants,
                value=option_random_restaurant,
                clearable=False,
                className="dropdown",
            )
        ]),
        html.Div([
            html.Div('Idioma', className="menu-title"),
            dcc.Dropdown(
                id='language-filter',
                options=options_idioms,
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
                min_date_allowed=min_date,
                max_date_allowed=max_date,
                start_date=min_date,
                end_date=max_date,
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