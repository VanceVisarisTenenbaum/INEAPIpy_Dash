# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 15:57:25 2026

@author: mano
"""

from dash import html
from Components.UIComponents.Managers.UIManager import UIManager

UIM = UIManager()

def DeleteRowButton(row_lv1, row_lv2=None, is_pair=False):

    if is_pair:
        class_name = 'cross'
        class_2 = 'btn-delete-pair'
    else:
        class_name = 'trash-can'
        class_2 = 'btn-delete-card'


    comp = html.Button(
        children=html.Div('', className='svg ' + class_name),
        className='btn-delete ' + class_2,
        **{'id': UIM.id_generator('Input', 'EliminarFila', 'Button', row_lv1, row_lv2)}
    )
    return comp