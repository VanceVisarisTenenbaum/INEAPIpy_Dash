# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 17:20:54 2025

@author: mano
"""

from dash import Dash, html
import Components.SelectionBox as SB


def main():
    """Starts the App."""
    app = Dash()

    app.layout = html.Div(
        children=[SB.SelectionBoxComponent(1)]
    )
    app.run(debug=True)
    return None


if __name__ == '__main__':
    main()
