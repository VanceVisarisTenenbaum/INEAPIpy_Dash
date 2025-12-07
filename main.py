# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 17:20:54 2025

@author: mano
"""

from dash import Dash, html
import Components.VarValPairsBox as VVPB


def main():
    """Starts the App."""
    app = Dash()

    app.layout = html.Div(
        children=[VVPB.VarValPairBoxComponent(1)]
    )
    app.run(debug=True)
    return None


if __name__ == '__main__':
    main()
