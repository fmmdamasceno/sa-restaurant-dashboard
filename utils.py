import pandas as pd
import nltk
from app import app

data = pd.read_csv(app.server.root_path+"/datasets/dataset.csv", dtype={'ano': 'object'})
data['data'] = pd.to_datetime(data.ano, format='%Y')

def stopwords():
    return nltk.corpus.stopwords.words()

def load_dataset():
    
    data = pd.read_csv(app.server.root_path+"/datasets/dataset.csv", dtype={'ano': 'object'})
    data['data'] = pd.to_datetime(data.ano, format='%Y')

    return data