# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 17:20:54 2025

@author: mano
"""

from dash import Dash, html
from Components.UIComponents.Main import initial_layout


def main():
    """Starts the App."""


    """Iniciamos el servidor de dash."""
    app = Dash(
        __name__,
        title='Datos Abiertos INE No Oficial',
        meta_tags=[
            {
            "name": "description",
            "content": "Proyecto experimental no oficial y herramienta interactiva para facilitar el consumo de la API del INE y visualizar los resultados en gráficas."
            },
            {
            "name": "keywords",
            "content": "INE API tool, INE API visualizer, consumir INE API, dashboard INE API, visualización de datos, Dash, Python"
            },
        ]
    )


    app.layout = html.Div(
        children=[
            initial_layout()
        ]
    )
    app.run(debug=True)
    return None


if __name__ == '__main__':
    main()
