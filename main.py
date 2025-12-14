# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 17:20:54 2025

@author: mano
"""

from dash import Dash, html, dcc
import Components.SelectionBox as SB


def main():
    """Starts the App."""


    """
    Definimos un almacenamiento que se generará una única vez y se utilizará para
    memoizar el uso que le de el usuario y sera únicamente válido mientras dure
    la sesión.
    """
    initial_storage = {
        'Variables': dict(),
        'Valores': dict(),
        'Tablas': dict(),
        'Periodo': dict(),
        'OperacionesSolicitadas': set(),  # To store the requested operations
        'VariablesSolicitadas': set(),  # To store the requested variables.
    }
    SESSION_STORAGE = dcc.Store(**{'id': 'SessionStorage',
                                   'storage_type': 'session'},
                                data=initial_storage)


    """Iniciamos el servidor de dash."""
    app = Dash()

    app.layout = html.Div(
        children=[
            SESSION_STORAGE,
            SB.SelectionBoxComponent(1)
        ]
    )
    SB.event_listeners_adder(1)
    app.run(debug=True)
    return None


if __name__ == '__main__':
    main()
