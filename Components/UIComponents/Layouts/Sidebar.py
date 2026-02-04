# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 17:06:43 2026

@author: mano
"""

from dash import html


def Sidebar():
    comp = html.Aside(
        children=[],
        className='sidebar'
    )
    return comp