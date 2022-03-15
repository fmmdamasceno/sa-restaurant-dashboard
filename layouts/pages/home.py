from dash import html
from dash import dcc
from layouts.pages import menu, header, footer
from layouts.components import (
    distribution,
    restaurant_rating,
    word_cloud,
    gender,
    rating_distribution,
    reviews_classification,
    top_reviewers,
    distribution_by_platform,
    character_count
)
from utils import (
    options_restaurants_all,
    options_idioms_all,
    min_date,
    max_date
)

layout = html.Div([
    menu.layout,
    header.layout,
    html.Div([
        html.Div([
            html.H1("Principal - Análise individual",style={'text-align':'center'})
        ]),
        html.Div([
            html.Div([
                html.Div('Restaurante'),
                dcc.Dropdown(
                    id='restaurant-filter',
                    options=options_restaurants_all,
                    value='Todos',
                    clearable=False,
                    className='dropdown',
                    style={
                        'color': 'gray'
                    }
                )
            ], className='form-group col-md-4'),
            html.Div([
                html.Div('Idioma'),
                dcc.Dropdown(
                    id='language-filter',
                    options=options_idioms_all,
                    value='Todos',
                    clearable=False,
                    className='dropdown',
                    style={
                        'color': 'gray',
                    },
                )
            ], className='form-group col-md-4'),
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
            ], className='form-group col-md-4')
        ],className='row card-body'),
    ], className='form-control container-fluid'),
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
            character_count.layout,
            distribution.layout,
            distribution_by_platform.layout
        ],className='row'),
    ], className="container-fluid"),
    footer.layout
],className="container-fluid")