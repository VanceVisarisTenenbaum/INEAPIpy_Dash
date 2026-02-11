# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 18:54:30 2026

@author: mano
"""

from dash import html

from Components.UIComponents.Arrangers.SeriesTableSelector import (TableContainer,
                                                                   TableTitle)

def SeriesSection():
    comp = html.Section(
        children=[
            TableTitle(),
            TableContainer()
        ],
        className='top-section-container'
    )
    return comp