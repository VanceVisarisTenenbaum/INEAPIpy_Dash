# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 16:15:09 2026

@author: mano
"""

from dash import clientside_callback, ClientsideFunction, Input, State, Output

def add_sidebar_toggle_event_listener():

    clientside_callback(
        ClientsideFunction(
            namespace='sidebar_toggle',
            function_name='toggle'
        ),
        Output('app-body', 'data-checked'),
        Input('hamburger-btn-label', 'n_clicks'),
        State('app-body', 'data-checked'),
        prevent_initial_call=True
    )
    return None