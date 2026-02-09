# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 18:48:55 2026

@author: mano
"""

from dash import html

from Components.UIComponents.Layouts.SeriesBox import SeriesSection
from Components.UIComponents.Layouts.GraphBox import GraphSection


def GraphSeriesContainer():
    comp = html.Main(
        children=[
            SeriesSection(),
            GraphSection()
        ],
        className='graph-series-container'
    )
    return comp