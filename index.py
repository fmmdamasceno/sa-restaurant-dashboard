from dash import dcc, html
from dash.dependencies import Output, Input
from app import app
from layouts import home, compare


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),

    # dcc.Store inside the user's current browser session
    dcc.Store(id='store-data', data=[], storage_type='memory') # 'local' or 'session'
])

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname'))
def display_page(pathname):
    if pathname in ('','/'):
        return home.layout
    elif pathname == '/compare':
        return compare.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)


