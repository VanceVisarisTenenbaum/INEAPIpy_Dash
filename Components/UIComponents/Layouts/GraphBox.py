# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 18:57:11 2026

@author: mano
"""

from dash import html

from Components.UIComponents.Arrangers.GraphArranger import (GraphTitle,
                                                             GraphContainer)


def GraphSection():
    comp = html.Div(
        children=[
            GraphTitle(),
            GraphContainer()
        ],
        className='graph-table-common bottom-section-container'
    )
    return comp