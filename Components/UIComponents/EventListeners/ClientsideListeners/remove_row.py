# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 21:41:54 2026

@author: mano
"""

from dash import clientside_callback, ClientsideFunction
from Components.UIComponents.Managers.UIManager import UIManager



UIM = UIManager()

def remove_row_event_listener():

    clientside_callback(
        ClientsideFunction(
            namespace='remove_row',
            function_name='remove_filter_row'
        ),
       inputs=UIM.io_generator(
            'Input', 'n_clicks',
            ui_type='Input',
            ui_name='EliminarFila',
            ui_subtype='Button',
            row_lv1='ALL'
        ),
        output=UIM.io_generator(
            'Output', 'children',
            ui_type='Arranger',
            ui_name='FilterSelection',
            ui_subtype=None,
        ),
        prevent_initial_call=True,
        allow_duplicates=True
    )

    clientside_callback(
        ClientsideFunction(
            namespace='remove_row',
            function_name='remove_var_val_row'
        ),
       inputs=UIM.io_generator(
           'Input', 'n_clicks',
           ui_type='Input',
           ui_name='EliminarFila',
           ui_subtype='Button',
           row_lv1='ALL',
           row_lv2='ALL'
       ),
       output=UIM.io_generator(
           'Output', 'children',
           ui_type='Arranger',
           ui_name='ParesVariableValor',
           ui_subtype=None,
           row_lv1='ALL',
           row_lv2=None
       ),
       prevent_initial_call=True,
       allow_duplicates=True
    )
    return None