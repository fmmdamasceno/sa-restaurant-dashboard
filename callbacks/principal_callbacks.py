from dash.dependencies import Input, Output
from app import app
from wordcloud import WordCloud
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import utils



@app.callback(
    Output('store', 'data'),
    Input('restaurant-filter', 'value'),
    Input('language-filter', 'value'),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
)
def select_restaurant(restaurant, language, start_date, end_date):
    restaurants = [restaurant]

    if restaurant == 'Todos':
        restaurants = utils.data.restaurante.unique()
    
    return utils.get_restaurants(restaurants, language, start_date, end_date).to_dict()
    

@app.callback(
    Output('restaurant-rating', 'figure'),
    Input('store', 'data')
)
def update_figure_restaurant_ratings(data):

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

# WordCloud Callback
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

    fig = px.imshow(wordcloud.to_image())
    fig.update_layout(margin=dict(l=20, r=20, t=10, b=10))
    return fig


# Distribution Callback
@app.callback(
    Output('comment-distribution', 'figure'),
    Input('store', 'data')
)
def update_distribution(data):

    selected_restaurant = pd.DataFrame(data).index
    
    df_coment_count = utils.data[['restaurante','fonte']].value_counts().reset_index(name='comentarios')

    dftable = pd.pivot_table(
        df_coment_count, values='comentarios', index='restaurante', columns='fonte')

    
    dftable = dftable.fillna(0).astype('int64')
    dftable['Total'] = dftable.sum(axis=1)


    
    fig = go.Figure(data=[go.Table( 
        header=dict(values=list(dftable.reset_index(level=0).columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[
                        dftable.index, dftable.Facebook, dftable.Foursquare, dftable.Google,
                        dftable.Guru, dftable.Yelp, dftable.Zomato, dftable.Total],
                fill_color='lavender',
                align='left'))
    ])
    
    fig.update_layout(margin=dict(l=20, r=20, t=10, b=10))
    return fig

# Gender distribution

@app.callback(
    Output('gender-distribution', 'figure'),
    Input('store', 'data')
)
def update_gender_distribution(data):
    df = pd.DataFrame(data)
    fig = px.pie(df,
             values=df.genero.value_counts().values,
             names=df.genero.value_counts().index)
    
    fig.update_layout(margin=dict(l=20, r=20, t=10, b=10))
    
    return fig

# Review Classification

@app.callback(
    Output('review-classification', 'figure'),
    Input('store', 'data')
)
def update_review_classification(data):
    df = pd.DataFrame(data)

    fig = px.pie(df,
             values=df.classificacao.value_counts().values,
             names=df.classificacao.value_counts().index, hole=0.5)

    fig.update_layout(margin=dict(l=20, r=20, t=10, b=10))
    return fig

# Rating distribution

@app.callback(
    Output('rating-distribution', 'figure'),
    Input('store', 'data')
)
def update_rating_distribution(data):

    df = pd.DataFrame(data).rating.value_counts()
    df.sort_index(ascending=False, inplace=True)
    

    fig = px.pie(df,
             values=df.values,
             names=df.index, hole=0.5)

    fig.update_traces(sort=False)
    fig.update_layout(
        margin=dict(l=20, r=20, t=10, b=10)
    )

    return fig

# Top Reviewers
    
@app.callback(
    Output('top-reviewers', 'figure'),
    Input('store', 'data')
)
def update_top_reviewers(data):
    df = pd.DataFrame(data)
    df = df.autor.value_counts().head(20)
    df.sort_values(ascending=True, inplace=True)

    fig = px.bar(
        df.sort_values(ascending=False),
        x=df.values,
        y=df.index,
        orientation='h')

    fig.update_layout(margin=dict(l=20, r=20, t=10, b=10))
    return fig

