# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 15:18:19 2026

@author: mano
"""

from dash import clientside_callback, ClientsideFunction

from Components.UIComponents.Managers.UIManager import UIManager

UIM = UIManager()

def select_serie_event_listener():

    clientside_callback(
        ClientsideFunction(
            namespace='select_serie',
            function_name='select_serie_switch'
        ),
        inputs=UIM.io_generator(
            'Input', 'n_clicks',
            ui_type='Label',
            ui_name='Serie',
            ui_subtype='Row',
            row_lv1='MATCH'
        ),
        state=[
            UIM.io_generator(
                'State', 'data-checked',
                ui_type='Label',
                ui_name='Serie',
                ui_subtype='Row',
                row_lv1='MATCH'
            ),
            UIM.io_generator(
                'State', 'data-serie-id',
                ui_type='Label',
                ui_name='Serie',
                ui_subtype='Row',
                row_lv1='MATCH'
            )
        ],
        output=[
            UIM.io_generator(
                'Output', 'data-checked',
                ui_type='Label',
                ui_name='Serie',
                ui_subtype='Row',
                row_lv1='MATCH'
            )
        ],
        prevent_initial_call=True
    )

    return None