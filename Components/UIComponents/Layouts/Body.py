# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 15:55:06 2026

@author: mano
"""

from dash import html

from Components.UIComponents.Layouts.Header import Header
from Components.UIComponents.Layouts.Sidebar import Sidebar


def Body():

    comp = html.Div(
        children=[
            html.Div(
                [
                    Header(),
                    Sidebar()
                    # Main
                ],
                className='main-layout',
                **{'data-checked': 1, 'data-switch': 'light', 'id': 'app-body'}
            )
        ]
    )

    return comp