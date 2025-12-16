# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 17:00:16 2025

@author: mano
"""

from dash import html
from Components.UIComponents.Common.Styles import (LABEL_INPUT_STYLE_TOP,
                                                   LABEL_INPUT_STYLE_SIDE)

def LabelInput(label, inputComponent, style='top'):

    if style == 'top':
        component = html.Div(
            children=[html.Span(label), inputComponent],
            style=LABEL_INPUT_STYLE_TOP
        )
    elif style == 'side':
        component = html.Div(
            children=[html.Span(label), inputComponent],
            style=LABEL_INPUT_STYLE_SIDE
        )
    else:
        raise ValueError('style can only be "top" or "side"')
    return component