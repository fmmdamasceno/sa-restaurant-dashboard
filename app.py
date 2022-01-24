import dash
import dash_bootstrap_components as dbc

# external_stylesheets = [
#     {
#         "href": "https://fonts.googleapis.com/css2?"
#         "family=Lato:wght@400;700&display=swap",
#         "rel": "stylesheet",
#     },
# ]

external_stylesheets = [dbc.themes.QUARTZ]

app = dash.Dash(
    __name__, suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets)

app.title = 'Restaurant Analytic Dashboard'