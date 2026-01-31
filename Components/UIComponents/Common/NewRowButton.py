# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 19:01:32 2026

@author: mano
"""

from dash import html
from Components.UIComponents.Managers.UIManager import UIManager


UIM = UIManager()
def NewRowButtonComp(name, row_lv1=None):

    boton = html.Button(
        'Nueva fila',
        n_clicks=0,
        **{'id': UIM.id_generator(ui_type='Input',
                                  ui_name=name,
                                  ui_subtype='Button',
                                  row_lv1=row_lv1)},
        className = 'Button'
    )
    comp = html.Div(
        children = [boton],
        className = 'ButtonContainer'
    )
    return comp