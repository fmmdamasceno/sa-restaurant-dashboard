from dash.dependencies import Input, Output
from app import app
from wordcloud import WordCloud
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import utils



@app.callback(
    Output('restaurant-rating-compare', 'figure'),
    Input('restaurant-filter-compare', 'value'),
    Input('language-filter-compare', 'value'),
    Input("date-range-compare", "start_date"),
    Input("date-range-compare", "end_date"),
)
def update_figure_restaurant_ratings_compare(restaurants, language, start_date, end_date):
    filtered_data = utils.get_restaurants(
        restaurants, language, start_date, end_date).groupby(['restaurante','ano'],as_index=False
    )['rating'].mean()

    fig = px.line(
        filtered_data,
        x='ano',
        y='rating',
        color='restaurante',
        labels={'ano':'Ano','rating':'Rating','restaurante':'Restaurante'})
    fig.update_traces(mode='markers+lines')
    return fig