import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dash.html.Figure import Figure
import pandas as pd
import numpy as np
import plotly.express as px



data = pd.read_csv("data/dataset.csv", dtype={'ano': 'object'})

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = 'Restaurant Analytic Dashboard'

app.layout = html.Div([
    html.Div([
        html.P('📈', className="header-emoji"),
        html.H1("Restaurant Analytic Dashboard", className="header-title"),
        html.P("Análise de comentários das plataformas de restaurantes Michelin no Brasil"
               " no período entre 2014 e 2020",
            className="header-description",
        ),
    ],className="header"),
    html.Div([
        html.Div([
            html.Div('Rating Médio', className="menu-title"),
            dcc.Dropdown(
                id='restaurant-filter',
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
                id='language-filter',
                options=[
                    {'label': language, 'value': language}
                    for language in np.sort(data.idioma.fillna('Any').unique())
                ],
                value='Any',
                clearable=False,
                className="dropdown",
            )
        ])
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
])


@app.callback(
    Output('restaurant-rating', 'figure'),
    Input('restaurant-filter', 'value'),
    Input('language-filter', 'value'),
)
def update_figure_restaurant_ratings(restaurants, language):
    search_filter = (
        (data.restaurante.isin(restaurants))
    )
    if language != 'Any':
        search_filter = search_filter & (data.idioma == language)

    filtered_data = data.loc[search_filter, :].groupby(
            ['restaurante','ano'],
            as_index=False)['rating'].mean()

    fig = px.line(
        filtered_data,
        x='ano',
        y='rating',
        color='restaurante',
        labels={'ano':'Ano','rating':'Rating','restaurante':'Restaurante'})
    fig.update_traces(mode='markers+lines')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)