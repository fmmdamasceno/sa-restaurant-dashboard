from dash import html
from dash import dcc
from layouts import menu, header, footer
from layouts.components import (
    distribution,
    restaurant_rating,
    word_cloud,
    gender,
    rating_distribution,
    reviews_classification,
    top_reviewers
)
from utils import (
    options_restaurants,
    options_idioms,
    option_random_restaurant,
    min_date,
    max_date
)

layout = html.Div([
    menu.layout,
    header.layout,
    html.Div([
        html.Div([
            html.Div([
                html.Div('Restaurante'),
                dcc.Dropdown(
                    id='restaurant-filter',
                    options=options_restaurants,
                    value=option_random_restaurant,
                    clearable=False,
                    className='dropdown',
                    style={
                        'color': 'gray'
                    }
                )
            ], className='dropdown'),
            html.Div([
                html.Div('Idioma'),
                dcc.Dropdown(
                    id='language-filter',
                    options=options_idioms,
                    value='Any',
                    clearable=False,
                    className='dropdown',
                    style={
                        'color': 'gray'
                    }
                )
            ], className=''),
            html.Div([
                html.Div("Período"),
                dcc.DatePickerRange(
                    id="date-range",
                    min_date_allowed=min_date,
                    max_date_allowed=max_date,
                    start_date=min_date,
                    end_date=max_date,
                    style={
                    }
                ),
            ], className='date')
        ],className='form-control'),
    ], className='container'),
    html.Br(),
    html.Div([
        html.Div([
            top_reviewers.layout,
            reviews_classification.layout,
            restaurant_rating.layout,
        ], className='row'),
        html.Br(),
        html.Div([
            rating_distribution.layout,
            gender.layout,
            word_cloud.layout,
        ],className='row'),
        html.Br(),
        html.Div([
            distribution.layout,
        ],className='row'),
        # distribution.layout,
        # word_cloud.layout,
        # restaurant_rating.layout,
        # gender.layout,
        # rating_distribution.layout,
        # reviews_classification.layout,
        # top_reviewers.layout
    ], className="container-fluid"),
    footer.layout
],className="container-fluid")