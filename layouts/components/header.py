from dash import html, dcc

layout = html.Div([
    
    html.Div([
        dcc.Link('Home', href='/', className='menu-title iblock'),
        html.Div([' '],className='iblock'),
        dcc.Link('Compare', href='/compare', className='menu-title iblock'),
        html.Div([' '],className='iblock'),
        dcc.Link('Explore', href='/explore', className='menu-title iblock')
    ],className=''),
    
    html.Div([
        html.H1("Restaurant Analytic Dashboard", className="header-title"),
        html.P("Análise de comentários das plataformas de restaurantes Michelin no Brasil"
               " no período entre 2014 e 2020",
            className="header-description",
        ),
    ],className="header"),
])

