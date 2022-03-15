from dash import html
from dash import dcc
from layouts.pages import menu, header, footer



layout = html.Div([
    menu.layout,
    header.layout,
    html.Div([
        html.H1("Sobre", style={'text-align':'center'})
    ]),
    html.Div([
        dcc.Markdown('''
        Este projeto foi desenvolvido por **Francisco Marcelo Mendes Damasceno** sob a orientação do **Prof. Dr. Tiago Eugenio de Melo**, como trabalho final de conclusão do curso de **Pós-Graduação *Latu Sensu* em Ciência de Dados** ofertado pela **Escola Superior de Tecnologia** da **Universidade do Estado do Amazonas (UEA)**.
       
        ***Resumo***

        Visualização de dados é essencial no processo análise de um determinado conjunto de dados. Neste cenário a utilização de *dashboards* tem se tornado cada vez mais comum, uma vez que este tipo de ferramenta potencializa o processo de análise e dá um feedback imediato sobre características desses dados. Infelizmente, grande parte das soluções de dashboard no mercado são proprietárias, e consequentemente pouco flexíveis com relação à customização e adaptação. Além disso, não existem muitos trabalhos na literatura sobre a construção de dashboards de forma geral, e no caso da língua portuguesa essa lacuna é ainda mais acentuada. Esse trabalho se propõe a construir um dashboard dinâmico direcionado para um conjunto de dados específicos, porém extensível e adaptável para outros domínios, fundamentado em plataformas opensource, cujo código está publicado e acessível no [**github**](https://github.com/fmmdamasceno/sa-restaurant-dashboard). Como base para este trabalho foi utilizado o resultado do estudo Análise de Comentários das Plataformas Online de Restaurantes Michelin no Brasil desenvolvido por Melo (2021),e ao final foi possível realizar uma análise comparativa entre os diversos restaurantes, com relação a média das avaliações, gênero, polaridade e outros aspectos do conjunto de dados utilizados.

        
        **Agradecimentos**

        Os autores agradecem ao Laboratório de Sistemas Inteligentes da Universidade do Estado do Amazonas pela disponibilização dos recursos computacionais que viabilizaram a realização deste trabalho.
        ''',
        style={
            'text-align': 'justify'
        })
    ], className='container'),
    
    footer.layout
])