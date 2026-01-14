# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 13:35:06 2025

@author: mano
"""

from dash import callback, ctx, clientside_callback, ClientsideFunction

from Components.Storage.StateStorage import StateStorageManager
from Components.UIComponents.Common.SelectComponent import SelectComponent
from Components.UIComponents.Common.ui_processes import (STORAGE_INPUTS,
                                                         STORAGE_OUTPUTS,
                                                         io_generator)


def ValorComponent(row_lv1, row_lv2, list_of_ine_val):
    component = SelectComponent(list_of_ine_val, 'Vl', row_lv1, row_lv2)
    return component



"""
Cuando el usuario seleccionar un valor ocurre lo siguiente:
    1- Se guarda el valor elegido en el almacenamiento de estado.

Los inputs necesarios son:
    3- El valor elegido, su fila 1 y fila 2.
    4- El almacenamiento de estado.

La salida debe ser:
    1- El almacenamiento de estado.
"""
SSM = StateStorageManager()
def server_side_listeners():
    """Adds the event listener to Valor Select"""
    @callback(
        STORAGE_OUTPUTS()[1],  # state
        io_generator('Input', 'Vl', None, 'ALL', 'ALL', 'value'),
        STORAGE_INPUTS()[1], # State storage
        prevent_initial_call=True
    )
    def process(val_id, state_storage):
        # Extraemos el valor elegido, la fila 1 y la fila 2
        val_id = ctx.triggered[0]['value']
        row_lv1 = ctx.triggered_id['fila_lv1']
        row_lv2 = ctx.triggered_id['fila_lv2']

        if not isinstance(val_id, int):
            return state_storage

        state_storage = SSM.update_selected_value(row_lv1,
                                                  row_lv2,
                                                  None, val_id,
                                                  state_storage)
        return state_storage
    return None


def client_event_listeners():

    clientside_callback(
        ClientsideFunction(
            namespace='clientside',
            function_name='update_selected_value'
        ),
        STORAGE_OUTPUTS()[1],  # state
        io_generator('Input', 'Vl', None, 'ALL', 'ALL', 'value'),
        STORAGE_INPUTS()[1], # State storage
        prevent_initial_call=True
    )


    return None

def valor_event_listener_adder():
    # server_side_listeners()
    client_event_listeners()
    return None