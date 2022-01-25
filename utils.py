import pandas as pd
import nltk
import numpy as np
import random
from app import app
from unidecode import unidecode

dfgenero = pd.read_csv(
    app.server.root_path+'/datasets/nomes.csv.gz'
)

males = dfgenero[dfgenero.classification == 'M'].first_name
females = dfgenero[dfgenero.classification == 'F'].first_name

def get_gender(name: str) -> str:
    fname = unidecode(name.split(' ')[0].upper())
    gender = 'Não identificado'
    if fname in males.to_list():
        gender = 'Masculino'
    elif fname in females.to_list():
        gender = 'Feminino'
    return gender

def review_classifcation(rating: int) -> str:
    if rating == 0:
        return 'Não informado'
    if rating >= 3:
        return 'Positivo'
    return 'Negativo'

data = pd.read_csv(
    app.server.root_path+"/datasets/dataset.csv",
    parse_dates=['ano'])

data['data'] = pd.to_datetime(data.ano, format='%Y')

data['genero'] = data.autor.apply(get_gender)

data['classificacao'] = data.rating.apply(review_classifcation)

columns = [{"name": i, "id": i} for i in data.columns]

max_date = data.data.max().date()
min_date = data.data.min().date()

options_restaurants = [
    {'label': restaurant, 'value': restaurant}
    for restaurant in np.sort(data.restaurante.unique())
]



options_restaurants_all = [{'label': 'Todos', 'value': 'Todos'}] + options_restaurants

option_random_restaurant = random.choice(
    [r for r in np.sort(data.restaurante.unique())]
)

options_idioms = [
    {'label': language, 'value': language}
    for language in np.sort(data.idioma.fillna('desconhecido').unique())
]

options_idioms_all = [{'label': 'Todos', 'value': 'Todos'}] + options_idioms

stopwords = nltk.corpus.stopwords.words()

def get_restaurants(restaurants, language, start_date, end_date):
    
    search_filter = (
        (data.restaurante.isin(restaurants))
        & (data.data >= start_date)
        & (data.data <= end_date)
    )
    if language != 'Todos':
        search_filter = search_filter & (data.idioma == language)

    return data.loc[search_filter, :]