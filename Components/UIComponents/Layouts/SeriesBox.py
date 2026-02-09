# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 18:54:30 2026

@author: mano
"""

from dash import html

def SeriesSection():
    comp = html.Section(
        children=[
            html.Div(
                children=[
                    html.H3('---------------  AAAAAAAA  -------------')
                ],
                className='table-scroll-area'
            )
        ],
        className='top-section-container'
    )
    return comp