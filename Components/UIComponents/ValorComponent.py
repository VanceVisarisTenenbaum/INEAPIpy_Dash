# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 13:35:06 2025

@author: mano
"""

from dash import callback, Input, Output, State

from Components.Storage.StateStorage import StateStorageManager
from Components.UIComponents.Common.SelectComponent import SelectComponent
from Components.UIComponents.Common.id_generator import id_generator_mapper

def ValorComponent(row_lv1, row_lv2, list_of_ine_val):
    component = SelectComponent(list_of_ine_val, 'Vl', row_lv1, row_lv2)
    return component



"""
Cuando el usuario seleccionar un valor ocurre lo siguiente:
    1- Se guarda el valor elegido en el almacenamiento de estado.

Los inputs necesarios son:
    1- La operación elegida previamente.
    2- La variable elegida previamente.
    3- El valor elegido.
    4- El almacenamiento de estado.

La salida debe ser:
    1- El almacenamiento de estado.
"""
SSM = StateStorageManager()
def valor_event_listener_adder(row_lv1, row_lv2):
    """Adds the event listener to Valor Select"""
    @callback(
        Output('StateStorage', 'data'),
        State(
            id_generator_mapper('O', None, row_lv1),
            'value'
        ),
        State(
            id_generator_mapper('Vr', None, row_lv1, row_lv2),
            'value'
        ),
        Input(
            id_generator_mapper('Vl', None, row_lv1, row_lv2),
            'value'
        ),
        State('ResquestsStorage', 'data'),
        State('StateStorage', 'data')
    )
    def process(op_id, var_id, val_id, state_storage):
        if not isinstance(val_id, int):
            return state_storage
        state_storage = SSM.update_selected_value(op_id,
                                                  var_id,
                                                  None, val_id,
                                                  state_storage)
        return state_storage
    return None