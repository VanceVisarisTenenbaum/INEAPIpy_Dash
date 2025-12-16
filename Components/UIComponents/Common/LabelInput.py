# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 17:00:16 2025

@author: mano
"""

from dash import html
from Components.UIComponents.Common.Styles import COMMON_PADDING

def LabelInput(label, inputComponent, style='top'):

    if style == 'top':
        component = html.Div(
            children=[html.Span(label), inputComponent],
            style={'display': 'flex',
                   'flex-direction': 'column',
                   'alignItems': 'left',
                   'marginBottom': '20px',
                   'padding': COMMON_PADDING,
                   'font-size': '40px'}
        )
    elif style == 'side':
        component = html.Div(
            children=[html.Span(label), inputComponent],
            style={'display': 'block', 'marginTop': '20px'}
        )
    else:
        raise ValueError('style can only be "top" or "side"')
    return component