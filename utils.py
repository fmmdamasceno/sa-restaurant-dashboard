import pandas as pd
import nltk
from app import app
from flask_caching import Cache



def stopwords(lang):
    return nltk.corpus.stopwords.words(lang)

def load_dataset():
    
    data = pd.read_csv(app.server.root_path+"/datasets/dataset.csv", dtype={'ano': 'object'})
    data['data'] = pd.to_datetime(data.ano, format='%Y')

    return data