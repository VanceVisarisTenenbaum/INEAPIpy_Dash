# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 20:27:54 2026

@author: mano
"""

from dash import clientside_callback, ClientsideFunction
from Components.UIComponents.Managers.UIManager import UIManager


UIM = UIManager()
def store_input_to_state_event_listener():


    clientside_callback(
        ClientsideFunction(
            namespace='state_storage',
            function_name='store_selected'
        ),
        inputs=UIM.io_generator(
            'Input', 'value',
            ui_type='Input',
            ui_name='ALL',
            ui_subtype='Dropdown',
            row_lv1='ALL',
            row_lv2='ALL'
            ),
        state=[
            UIM.io_generator(
                'State', 'data',
                ui_type='Storage',
                ui_name='State',
            ),
            UIM.io_generator(
                'State', 'value',
                ui_type='Input',
                ui_name='Serie',
                ui_subtype='Dropdown',
                row_lv1='ALL'
            ),
        ],
        output=UIM.io_generator(
            'Output', 'data',
            ui_type='Storage',
            ui_name='State'
        ),
        prevent_initial_call=True
    )
    return None