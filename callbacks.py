from dash.dependencies import Input, Output
from app import app
from utils import data, stopwords
import plotly.express as px

import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

@app.callback(
    Output('restaurant-rating-compare', 'figure'),
    Input('restaurant-filter-compare', 'value'),
    Input('language-filter-compare', 'value'),
    Input("date-range-compare", "start_date"),
    Input("date-range-compare", "end_date"),
)
def update_figure_restaurant_ratings_compare(restaurants, language, start_date, end_date):
    search_filter = (
        (data.restaurante.isin(restaurants))
        & (data.data >= start_date)
        & (data.data <= end_date)
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

@app.callback(
    Output('restaurant-rating', 'figure'),
    Input('restaurant-filter', 'value'),
    Input('language-filter', 'value'),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
)
def update_figure_restaurant_ratings(restaurant, language, start_date, end_date):
    search_filter = (
        (data.restaurante == restaurant)
        & (data.data >= start_date)
        & (data.data <= end_date)
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
        labels={'ano':'Ano','rating':'Rating','restaurante':'Restaurante'},
        title="Avaliação Média", height=400)
    fig.update_traces(mode='markers+lines')
    return fig


@app.callback(
    Output('restaurant-wordcloud', 'figure'),
    Input('restaurant-filter', 'value'),
    Input('language-filter', 'value'),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
)
def update_wordcloud(restaurant, language, start_date, end_date):
    search_filter = (
        (data.restaurante == restaurant)
        & (data.data >= start_date)
        & (data.data <= end_date)
    )
    if language != 'Any':
        search_filter = search_filter & (data.idioma == language)

    filtered_data = data.loc[search_filter, :].dropna(subset=['comentario'], axis=0)['comentario']
    
    concat_words = " ".join(s for s in filtered_data)

    wordcloud = WordCloud(
        stopwords=stopwords,
        background_color="black",
        width=1600, height=800).generate(concat_words)

    fig = px.imshow(wordcloud.to_image(),title="Nuvem de Palavras")
    return fig



