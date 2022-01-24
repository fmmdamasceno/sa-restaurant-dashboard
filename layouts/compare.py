from dash import html
from dash import dcc
from layouts.components import menu, header, footer
from utils import (
    options_restaurants,
    options_idioms,
    min_date,
    max_date
)

layout = html.Div([
    menu.layout,
    header.layout,
    html.Div([
        html.Div([
            html.Div([
                html.Div('Restaurante', className="menu-title"),
                dcc.Dropdown(
                    id='restaurant-filter-compare',
                    options=options_restaurants,
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
                    id="date-range-compare",
                    min_date_allowed=min_date,
                    max_date_allowed=max_date,
                    start_date=min_date,
                    end_date=max_date,
                ),
            ]),
        ], className="form-control")
    ],className="container"),
    html.Br(),
    html.Div([
        html.Div([
            html.H5(['Rating Médio - Coparativo'], className='card-title'),
            dcc.Graph(
                id="restaurant-rating-compare",
                config={"displayModeBar": False},
            )
        ],className="card-body p-1"),
    ],className="card"),
    footer.layout
])
