import base64
import io
import os

from use_api.pdf2txt import convert_pdf
import dash_html_components as html


def treat_files(contents, filename, date):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    try:
        temporarylocation = filename
        with open(temporarylocation, 'wb') as out:  ## Open temporary file as bytes
            out.write(io.BytesIO(decoded).read())  ## Read bytes into file
        txt = convert_pdf(temporarylocation)
        os.remove(temporarylocation)  ## Delete file when done

    except Exception as e:
        print(e)
        return html.Div([
            str(e) + 'There was an error processing this file.'
        ])

    div = html.Div([
        html.H5(filename),
        # TODO add button to download file
        html.Hr(),  # horizontal line
        html.H6(txt),
    ])

    return div