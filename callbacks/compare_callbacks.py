from dash.dependencies import Input, Output
from app import app
from wordcloud import WordCloud
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import utils



@app.callback(
    Output('store-compare', 'data'),
    Input('restaurant-filter-compare', 'value'),
    Input('language-filter-compare', 'value'),
    Input("date-range-compare", "start_date"),
    Input("date-range-compare", "end_date"),
)
def select_restaurant(restaurants, language, start_date, end_date):
    
    return utils.get_restaurants(restaurants, language, start_date, end_date).to_dict()


# Average Rating 
@app.callback(
    Output('restaurant-rating-compare', 'figure'),
    Input('store-compare', 'data')
)
def update_figure_restaurant_ratings_compare(data):
    
    filtered_data = pd.DataFrame(data).groupby(
            ['restaurante','data'],
            as_index=False)['rating'].mean()

    fig = px.line(
        filtered_data,
        x='data',
        y='rating',
        color='restaurante',
        labels={'data':'Data','rating':'Rating','restaurante':'Restaurante'})
    
    fig.update_layout(margin=dict(l=20, r=20, t=10, b=10))
    fig.update_traces(mode='markers+lines')
    return fig


# Gender distribution

@app.callback(
    Output('gender-distribution-compare', 'figure'),
    Input('store-compare', 'data')
)
def update_gender_distribution(data):
    df = pd.DataFrame(data)
    
    restaurants = list(df.restaurante.unique())

    fig = {}

    restaurant_count = len(restaurants)

    if restaurant_count > 1:

        fig = make_subplots(
            rows=1, cols=len(restaurants),
            subplot_titles=[r.capitalize() for r in restaurants],
            specs=[restaurant_count * [{'type':'domain'}]]
        )

        for idx,restaurant in enumerate(restaurants):
            fig.add_trace(
                go.Pie(
                    labels=df[df.restaurante == restaurant].genero.value_counts().index,
                    values=df[df.restaurante == restaurant].genero.value_counts().values,
                    name=restaurant.capitalize()), 1, idx+1)

        fig.update_traces(hole=0.5)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=10))
    
    return fig


# Review Classification

@app.callback(
    Output('review-classification-compare', 'figure'),
    Input('store-compare', 'data')
)
def update_review_classification(data):
    df = pd.DataFrame(data)
    
    restaurants = list(df.restaurante.unique())

    fig = {}

    restaurant_count = len(restaurants)

    if restaurant_count > 1:

        fig = make_subplots(
            rows=1, cols=len(restaurants),
            subplot_titles=[r.capitalize() for r in restaurants],
            specs=[restaurant_count * [{'type':'domain'}]]
        )

        for idx,restaurant in enumerate(restaurants):
            fig.add_trace(
                go.Pie(
                    labels=df[df.restaurante == restaurant].classificacao.value_counts().index,
                    values=df[df.restaurante == restaurant].classificacao.value_counts().values,
                    name=restaurant.capitalize()), 1, idx+1)

        fig.update_traces(hole=0.5)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=10))
    
    return fig


# Rating distribution

@app.callback(
    Output('rating-distribution-compare', 'figure'),
    Input('store-compare', 'data')
)
def update_rating_distribution(data):

    df = pd.DataFrame(data)
    df.sort_index(ascending=False, inplace=True)
    
    restaurants = list(df.restaurante.unique())

    fig = {}

    restaurant_count = len(restaurants)

    if restaurant_count > 1:

        fig = make_subplots(
            rows=1, cols=len(restaurants),
            subplot_titles=[r.capitalize() for r in restaurants],
            specs=[restaurant_count * [{'type':'domain'}]]
        )

        for idx,restaurant in enumerate(restaurants):
            dfr = df[df.restaurante == restaurant].rating.value_counts()
            dfr.sort_index(ascending=False, inplace=True)

            fig.add_trace(
                go.Pie(
                    labels=dfr.index,
                    values=dfr.values,
                    name=restaurant.capitalize()), 1, idx+1)

        fig.update_traces(hole=0.5, sort=False)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=10))
    

    return fig