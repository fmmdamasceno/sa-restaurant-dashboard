import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dash.html.Figure import Figure
import pandas as pd
import numpy as np
import plotly.express as px



data = pd.read_csv("data/dataset.csv", dtype={'ano': 'object'})

app = dash.Dash(__name__)


app.layout = html.Div([
    html.Label('Escolha um ou mais Restaurantes'),
    html.Br(),
    dcc.Dropdown(
        id='restaurant-filter',
        options=[
            {'label': restaurant, 'value': restaurant}
            for restaurant in np.sort(data.restaurante.unique())
        ],
        multi=True,
        value=[]
    ),
    dcc.Graph(
        id="restaurant-rating",
        
    ),

])


@app.callback(
    Output('restaurant-rating', 'figure'),
    Input('restaurant-filter', 'value')
)
def update_figure_restaurant_ratings(restaurants):
    search_filter = (
        (data.restaurante.isin(restaurants))
    )
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