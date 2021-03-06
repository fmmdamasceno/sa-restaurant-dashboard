from dash import html, dcc

layout = html.Div([
    
    html.Ul([
        html.Li([
            dcc.Link('Principal', href='/', className='nav-link')
        ], className='nav-item'),
        html.Li([
            dcc.Link('Compare', href='/compare', className='nav-link')
        ], className='nav-item'),
        html.Li([
            dcc.Link('Explore', href='/explore', className='nav-link')
        ], className='nav-item'),
        html.Li([
            dcc.Link('Sobre', href='/about', className='nav-link')
        ], className='nav-item'),
    ],className='nav nav-pills')
], className='container-fluid')