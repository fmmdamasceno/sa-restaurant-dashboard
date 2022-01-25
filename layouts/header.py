from dash import html, dcc

layout = html.Div([
    html.Div([
        html.H1(["Dashboard dinâmico para mineração de opinião de restaurantes estrelados no Brasil"]),
        html.P("Análise de comentários das plataformas de restaurantes Michelin no Brasil"
               " no período entre 2014 e 2020",   
        ),
    ],className=''),
], className='container')

