# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 17:20:54 2025

@author: mano
"""

from dash import Dash, html
import Components.UIComponents.SelectionBox as SB


def main():
    """Starts the App."""


    """Iniciamos el servidor de dash."""
    app = Dash()

    app.layout = html.Div(
        children=[
            SB.InputSelectionBox()
        ]
    )
    SB.event_listeners_adder(1)
    app.run(debug=True)
    return None


if __name__ == '__main__':
    main()
