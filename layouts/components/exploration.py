from pydoc import classname
from dash import html
from dash import dcc
from dash import dash_table as dt
from matplotlib.pyplot import gray
from app import app
from utils import columns, data


layout = html.Div([
    html.Div([
        html.Div([
            dt.DataTable(
                id='datatable-row-ids',
                columns=columns,
                data=data.to_dict('records'),
                filter_action="native",
                sort_action="native",
                sort_mode="multi",
                page_action="native",
                page_current= 0,
                page_size= 15,
                style_table={
                    'fontFamily': 'Open Sans',
                    'color': 'gray',
                    'maxHeight': '50ex',
                    'overflowY': 'scroll',
                    'width': '100%',
                    'minWidth': '100%'
                },
                style_data={
                    'whiteSpace': 'normal',
                    'height': 'auto',
                }
            ),
        ], className='card')
    ],className="container-fluid"),
],className='')
