import pandas as pd
import nltk
from app import app

data = pd.read_csv(app.server.root_path+"/datasets/dataset.csv", dtype={'ano': 'object'})
data['data'] = pd.to_datetime(data.ano, format='%Y')

stopwords = nltk.corpus.stopwords.words()

if __name__ == '__main__':
    pass