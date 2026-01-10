# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 19:01:32 2026

@author: mano
"""

from dash import html
from Components.UIComponents.Common.id_generator import id_generator_mapper

def NewRowButtonComp(row_lv1=None):
    if row_lv1 is None:
        name = 'O'
    else:
        name = 'VariableValor'
    boton = html.Button(
        'Nueva fila',
        n_clicks=0,
        **{'id': id_generator_mapper(name, 'Boton', row_lv1)},
        className = 'Button'
    )
    comp = html.Div(
        children = [boton],
        className = 'ButtonContainer'
    )
    return comp