from dash import dcc, html
from dash.dependencies import Output, Input
from app import app
from layouts import explore, home, compare, about
import callbacks


app.layout = html.Div([
    dcc.Store(id='store'),
    dcc.Store(id='parameters'),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname'))
def display_page(pathname):
    if pathname in ('','/'):
        return home.layout
    elif pathname == '/compare':
        return compare.layout
    elif pathname == '/explore':
        return explore.layout
    elif pathname == '/about':
        return about.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)


