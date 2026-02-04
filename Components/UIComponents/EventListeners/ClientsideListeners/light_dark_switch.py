# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 19:06:02 2026

@author: mano
"""

from dash import clientside_callback, ClientsideFunction, Input, Output, State


def add_light_dark_event_listener():

    clientside_callback(
        ClientsideFunction(
            namespace='light_dark_switch',
            function_name='switch_f'
        ),
        Output('app-body', 'data-switch'),
        Input('light-dark-switch-label', 'n_clicks'),
        State('app-body', 'data-switch'),
        prevent_initial_call=True
    )

    return None