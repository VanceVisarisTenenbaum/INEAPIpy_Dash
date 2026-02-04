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
        Output('sidebar-toggle', 'data-checked'),
        Input('hamburger-btn-label', 'n_clicks'),
        State('sidebar-toggle', 'data-checked')
    )
    return None