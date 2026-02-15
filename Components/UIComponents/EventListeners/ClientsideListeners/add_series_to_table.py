# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 16:06:17 2026

@author: mano
"""

from dash import clientside_callback, ClientsideFunction
from Components.UIComponents.Managers.UIManager import UIManager

UIM = UIManager()

def add_series_event_listener():
    clientside_callback(
        ClientsideFunction(
            namespace='add_series_to_table',
            function_name='add_series'
        ),
        inputs=UIM.io_generator(
            'Input', 'data',
            ui_type='Storage',
            ui_name='Dummy',
            ui_subtype='Series'
        ),
        output=UIM.io_generator(
            'Output', 'children',
            ui_type='Container',
            ui_name='Table'
        ),
        prevent_initial_call=True,
    )
    return None