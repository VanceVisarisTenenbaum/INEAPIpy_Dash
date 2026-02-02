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
            function_name='add_new_row'
        ),
       inputs=UIM.io_generator(
            'Input', 'n_clicks',
            ui_type='Input',
            ui_name='MATCH',
            ui_subtype='Button',
        ),
        output=UIM.io_generator(
            'Output', 'children',
            ui_type='Arranger',
            ui_name='MATCH',
            ui_subtype=None,
        ),
        prevent_initial_call=True
    )
    return None