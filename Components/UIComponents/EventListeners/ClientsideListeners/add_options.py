# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 18:17:19 2026

@author: mano
"""

from dash import clientside_callback, ClientsideFunction
from Components.UIComponents.Managers.UIManager import UIManager

UIM = UIManager()

def add_options_event_listener():

    clientside_callback(
        ClientsideFunction(
            namespace='add_options_to_inputs',
            function_name='add_options_to_inputs'
        ),
        inputs=UIM.io_generator(
            'Input', 'data',
            ui_type='Storage',
            ui_name='Dummy',
            ui_subtype='Client'
        ),
        prevent_initial_call=True
    )

    return None