FROM python:3.8
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN python -c 'import nltk;nltk.download("stopwords")'
CMD python index.py
