# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 20:44:33 2026

@author: mano
"""

from dash import clientside_callback, ClientsideFunction
from Components.UIComponents.Managers.UIManager import UIManager

UIM = UIManager()

def check_requested_event_listener():

    clientside_callback(
        ClientsideFunction(
            namespace='input_check',
            function_name='check_requested'
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
                ui_name='Dummy',
                ui_subtype='Server'
                ),
            UIM.io_generator(
                'State', 'data',
                ui_type='Storage',
                ui_name='Dummy',
                ui_subtype='Client'
                ),
        ],
        output=[
            UIM.io_generator(
                'Output', 'data',
                ui_type='Storage',
                ui_name='Dummy',
                ui_subtype='Server'
            ),
            UIM.io_generator(
                'Output', 'data',
                ui_type='Storage',
                ui_name='Dummy',
                ui_subtype='Client'
            )
        ],
        prevent_initial_call=True
    )

    return None