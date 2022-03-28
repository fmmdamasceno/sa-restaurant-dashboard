# Dashboard dinâmico para mineração de opinião de restaurantes estrelados no Brasil
### Análise de comentários das plataformas de restaurantes Michelin no Brasil no período entre 2014 e 2020

Este projeto foi desenvolvido por Francisco Marcelo Mendes Damasceno sob a orientação do Prof. Dr. Tiago Eugenio de Melo, como trabalho final de conclusão do curso de Pós-Graduação Latu Sensu em Ciência de Dados ofertado pela Escola Superior de Tecnologia da Universidade do Estado do Amazonas (UEA).
--

Demo: https://dashboard.marcelomendes.dev/

Como rodar esse projeto localmente?

1. Clonar o repositório

    <code>git clone https://github.com/fmmdamasceno/sa-restaurant-dashboard</code>

2. Criar um virtual environment (venvwrapper, pipenv, conda e afins)

3. Instalar as dependências

    <code>pip install -r requirements.txt</code>

    Download dos pacotes NLTK para stopwords

    <code>python -c 'import nltk;nltk.download("stopwords")'</code>

4. Executar o serviço:

    <code>python index.py</code>

5. Acessar em http://localhost:8050

