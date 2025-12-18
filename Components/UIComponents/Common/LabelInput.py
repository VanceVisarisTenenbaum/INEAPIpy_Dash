# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 17:00:16 2025

@author: mano
"""

from dash import html

def LabelInput(label, inputComponent, style='top'):

    if style == 'top':
        component = html.Div(
            children=[html.Span(label), inputComponent],
            className='LabelInput LITop'
        )
    elif style == 'side':
        component = html.Div(
            children=[html.Span(label), inputComponent],
            className='LabelInput LISide'
        )
    else:
        raise ValueError('style can only be "top" or "side"')
    return component