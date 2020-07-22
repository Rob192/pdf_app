import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from components.page_layout import app_page_layout
from components.file_loader import file_loader
from components.main_page_informations import explanation

from src.treat_files import treat_files


def layout():
    div = html.Div([
            explanation(),
            file_loader(),
            dbc.Spinner(
                id='spinner',
                children=[html.Div(id='output-data-upload')]
            )
        ])
    return div


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.title = "Pdf2txt"
app_title = "Pdf2txt"
app.config['suppress_callback_exceptions'] = True
# Assign layout
app.layout = app_page_layout(
    page_layout=layout(),
    app_title=app_title,
)


@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            # TODO do not remove output when page is moving
            treat_files(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)