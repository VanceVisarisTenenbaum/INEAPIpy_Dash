# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 16:50:20 2026

@author: mano
"""


from dash import clientside_callback, ClientsideFunction
from Components.UIComponents.Managers.UIManager import UIManager

UIM = UIManager()

def plot_graph_event_listener():

    clientside_callback(
        ClientsideFunction(namespace='plot_data', function_name='plot_graphs'),
        inputs=UIM.io_generator('Input', 'data',
                                ui_type='Storage',
                                ui_name='Dummy',
                                ui_subtype='Requested_Data'),
        state=[
            UIM.io_generator(
                'State', 'children',
                ui_type='Container',
                ui_name='Table'),
            UIM.io_generator(
                'State', 'id',
                ui_type='Input',
                ui_name='Grafica',
                ui_subtype='Dropdown',
                row_lv1='ALL'
            ),
            UIM.io_generator(
                'State', 'value',
                ui_type='Input',
                ui_name='Grafica',
                ui_subtype='Dropdown',
                row_lv1='ALL'
            ),
            UIM.io_generator(
                'State', 'id',
                ui_type='Input',
                ui_name='Eje Grafica',
                ui_subtype='Dropdown',
                row_lv1='ALL'
            ),
            UIM.io_generator(
                'State', 'value',
                ui_type='Input',
                ui_name='Eje Grafica',
                ui_subtype='Dropdown',
                row_lv1='ALL'
            )
        ],
        prevent_initial_call=True
    )

    return None