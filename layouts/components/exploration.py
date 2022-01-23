from dash import html
from dash import dcc
import dash_table as dt
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
                style_data={
                    'whiteSpace': 'normal',
                    'height': 'auto',
                    'lineHeight': '15px',
                },
            ),
        ], className='')
    ],className="card"),
],className="wrapper",)
