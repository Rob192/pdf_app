import dash_core_components as dcc
import dash_html_components as html

def explanation():
    EXPLANATION = dcc.Markdown("""
Faites glisser vos documents dans l'application pour les convertir en .txt
Vos documents ne sont pas stockés sur notre serveur. 
""")

    explanation = html.Div(
        id='explanation',
        children = [
            html.H4(className='what-is', children="Convertissez vos documents PDF en .txt"),
            html.P(EXPLANATION),
        ]
    )
    return explanation