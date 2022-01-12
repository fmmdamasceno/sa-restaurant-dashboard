from dash.dependencies import Input, Output
from app import app
from wordcloud import WordCloud
import plotly.express as px
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


@app.callback(
    Output('store', 'data'),
    Input('restaurant-filter', 'value'),
    Input('language-filter', 'value'),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
)
def select_restaurant(restaurant, language, start_date, end_date):
    return utils.get_restaurants([restaurant], language, start_date, end_date).to_dict()
    

@app.callback(
    Output('restaurant-rating', 'figure'),
    Input('store', 'data')
)
def update_figure_restaurant_ratings(data):

    filtered_data = pd.DataFrame(data).groupby(
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
    Input('store', 'data')
)
def update_wordcloud(data):

    filtered_data = pd.DataFrame(data).dropna(
        subset=['comentario'], axis=0)['comentario']
   
    concat_words = " ".join(s for s in filtered_data)

    wordcloud = WordCloud(
        stopwords=utils.stopwords,
        background_color="black",
        width=1600, height=800).generate(concat_words)

    fig = px.imshow(wordcloud.to_image(),title="Nuvem de Palavras")
    return fig