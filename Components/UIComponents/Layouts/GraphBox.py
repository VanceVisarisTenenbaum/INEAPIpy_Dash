# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 18:57:11 2026

@author: mano
"""

from dash import html

def GraphSection():
    comp = html.Div(
        children=[
            html.Div(
                children=[],
                className='charts-grid-wrapper'
            )
        ],
        className='bottom-section-container'
    )
    return comp