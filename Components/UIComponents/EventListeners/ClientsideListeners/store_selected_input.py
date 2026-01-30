# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 20:27:54 2026

@author: mano
"""

from dash import clientside_callback, ClientsideFunction
from Components.UIComponents.Common.ui_processes import (STORAGE_INPUTS,
                                                         STORAGE_OUTPUTS,
                                                         DUMMY_INPUT,
                                                         DUMMY_OUTPUT,
                                                         io_generator)



def store_input_to_state_event_listener():

    input_function_map = {
        'Operacion': 'update_selected_operation',
        'Tabla': 'update_selected_table',
        'Variable': 'update_selected_variable',
        'Valor': 'update_selected_value',
        'Serie': 'update_selected_serie',
        'Graph': 'update_selected_graph',
        'Graph Axis': 'update_selected_graph_axis',
        'Graph Style': 'update_selected_graph_style',
    }

    input_row_lv2_map = lambda x: 'ALL' if x in ['Variable', 'Valor'] else None


    for input_type in input_function_map.keys():
        if 'Graph' in input_type:
            clientside_callback(
                ClientsideFunction(
                    namespace='state_storage',
                    function_name=input_function_map[input_type]
                    ),
                io_generator('Input', input_type, None,
                             'ALL', None, 'value'),
                STORAGE_INPUTS()[1],  # State storage
                io_generator('State', 'S', None, 'ALL', None, 'value'),
                prevent_initial_call=True
            )
        else:
            clientside_callback(
                ClientsideFunction(
                    namespace='state_storage',
                    function_name=input_function_map[input_type]
                    ),
                io_generator('Input', input_type, None,
                             'ALL', input_row_lv2_map(input_type)),
                STORAGE_INPUTS()[1],  # State storage
                STORAGE_OUTPUTS()[1],  # State storage
                prevent_initial_call=True
            )

    return None