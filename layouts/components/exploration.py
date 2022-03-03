from pydoc import classname
from dash import html
from dash import dcc
from dash import dash_table as dt
from matplotlib.pyplot import gray
from app import app
from utils import columns, data


layout = html.Div([
    html.Div([
            html.H4("Realize uma exploração básica dos dados incluindo busca "
                   "por termo e ordenação, bastando digitar  o termo desejado "
                   "no campo logo abaixo de cada coluna.",   
            ),
    ],className='container'),
    html.Div([
        html.Div([
            html.H5(['Exploração dos dados'], className='card-title'),
            dt.DataTable(
                id='datatable-row-ids',
                columns=columns,
                data=data.to_dict('records'),
                filter_action="native",
                filter_query="teste",
                sort_action="native",
                sort_mode="multi",
                page_action="native",
                page_current= 0,
                page_size= 15,
                style_table={
                    'fontFamily': 'Open Sans',
                    'color': 'gray',
                    'maxHeight': '100ex',
                    'overflowY': 'scroll',
                    'width': '100%',
                    'minWidth': '100%',
                    'fontSize': '12px',
                    'placeholder':'teste'
                },
                style_data={
                    'whiteSpace': 'normal',
                    'height': 'auto',
                }
                
            ),
        ], className='card-body')
    ],className="card"),
],className='container-fluid')
