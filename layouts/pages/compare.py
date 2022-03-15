from dash import html
from dash import dcc
from layouts.pages import menu, header, footer
from layouts.components import (
    compare_gender,
    compare_restaurant_rating,
    compare_review_classification,
    compare_rating_distribution,
    compare_word_cloud
)
from utils import (
    options_restaurants,
    options_idioms_all,
    min_date,
    max_date
)

layout = html.Div([
    menu.layout,
    header.layout,
    html.Div([
        html.H1("Compare - Análise Comparativa", style={'text-align':'center'})
    ]),
    html.Div([
        html.Div([
            html.Div([
                html.Div('Restaurante'),
                dcc.Dropdown(
                    id='restaurant-filter-compare',
                    options=options_restaurants,
                    multi=True,
                    value=[],
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
                    id='language-filter-compare',
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
                    id="date-range-compare",
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
            compare_restaurant_rating.layout,
        ], className='row'),
        html.Br(),
        html.Div([
            compare_gender.layout,
        ],className='row'),
        html.Br(),
        html.Div([
            compare_review_classification.layout
        ],className='row'),
        html.Br(),
        html.Div([
            compare_rating_distribution.layout
        ],className='row'),
        html.Br(),
        html.Div([
            compare_word_cloud.layout,
        ], className='row'),
    ], className="container-fluid"),
    footer.layout
],className="container-fluid")