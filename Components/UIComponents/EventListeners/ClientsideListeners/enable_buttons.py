# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 10:32:44 2026

@author: mano
"""


from dash import clientside_callback, ClientsideFunction
from Components.UIComponents.Managers.UIManager import UIManager

UIM = UIManager()

def enable_buttons_event_listener():

    clientside_callback(
        ClientsideFunction(
            namespace='enable_buttons',
            function_name='enable_var_val_button'
        ),
        inputs=UIM.io_generator(
            'Input', 'value',
            ui_type='Input',
            ui_name='Operacion',
            ui_subtype='Dropdown',
            row_lv1='MATCH'
        ),
        output=UIM.io_generator(
            'Input', 'disabled',
            ui_type='Input',
            ui_name='ParesVariableValor',
            ui_subtype='Button',
            row_lv1='MATCH'
        ),
        prevent_initial_call=True
    )

    return None