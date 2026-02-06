# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 17:47:22 2026

@author: mano
"""

from dash import clientside_callback, ClientsideFunction
from Components.UIComponents.Managers.UIManager import UIManager



UIM = UIManager()
def add_new_row_event_listener():

    clientside_callback(
        ClientsideFunction(
            namespace='add_row',
            function_name='add_new_FR'
        ),
       inputs=UIM.io_generator(
            'Input', 'n_clicks',
            ui_type='Input',
            ui_name='Filtro',
            ui_subtype='Button',
        ),
        output=UIM.io_generator(
            'Output', 'children',
            ui_type='Arranger',
            ui_name='FilterSelection',
            ui_subtype=None,
        ),
        prevent_initial_call=True
    )

    clientside_callback(
        ClientsideFunction(
            namespace='add_row',
            function_name='add_new_var_val'
        ),
       inputs=UIM.io_generator(
           'Input', 'n_clicks',
           ui_type='Input',
           ui_name='ParesVariableValor',
           ui_subtype='Button',
           row_lv1='MATCH',
           row_lv2=None
       ),
       state=UIM.io_generator(
           'State', 'value',
           ui_type='Input',
           ui_name='Operacion',
           ui_subtype='Dropdown',
           row_lv1='MATCH',
           row_lv2=None
       ),
       output=UIM.io_generator(
           'Output', 'children',
           ui_type='Arranger',
           ui_name='ParesVariableValor',
           ui_subtype=None,
           row_lv1='MATCH',
           row_lv2=None
       ),
       prevent_initial_call=True
    )
    return None