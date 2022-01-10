import pandas as pd
import nltk

data = pd.read_csv("datasets/dataset.csv", dtype={'ano': 'object'})
data['data'] = pd.to_datetime(data.ano, format='%Y')

stopwords = nltk.corpus.stopwords.words()

if __name__ == '__main__':
    nltk.download('stopwords')