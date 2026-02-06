# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 17:06:43 2026

@author: mano
"""

from dash import html
from Components.UIComponents.Arrangers.FilterSelection import (FilterSelectionBox, make_FR)


def Sidebar():
    comp = html.Aside(
        children=[
            html.H2('Filtros', className='sidebar-title'),
            FilterSelectionBox(make_FR(1)),
        ],
        className='sidebar'
    )
    return comp