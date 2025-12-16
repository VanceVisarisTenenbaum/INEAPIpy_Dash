# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 11:42:49 2025

@author: mano
"""

from dash import dcc
from Components.Storage.SingletonCustom import SingletonMeta

"""
State Storage es un almacenamiento de sesión cuyo objetivo es almacenar todas
las decisiones tomadas por el usuario, de este modo se puede recuperar rápida
mente el estado de la sesión en caso de recargar la página.

Las decisiones que puede tomar el usuario son:
    1- Seleccionar una o varias operaciones.
    2- Seleccionar 0 o 1 tabla
    3- Seleccionar 0 o 1 o varios pares variable-valor.
    4- Seleccionar 0 o 1 o varias series.
    5- Seleccionar 1 Gráfica para la serie.
    6- Seleccinar 1 eje para la gráfica.
    7- Seleccionar 1 estilo para la gráfica.

Por este motivo, el session storage tiene la siguiente estructura:
    {
        op_id: {
            'Tabla': tab_id | None,
            'VariableValor': {var_id: val_id} | None
            'Serie': {
                 serie_id: {
                    'NGrafica': N_Grafica | None,
                    'Axis': EjeGrafica | None,
                    'Style': EstiloGrafica | None
                }
            }
        }
    }

Al igual que RequestsStorageManager, StateStorageManager es una instancia
de servidor, pero el estado en el que se encuentra la app es información
que se encuentra únicamente en la sesión del usuario, por este motivo, todos
los métodos toman como input el session_storage y lo devuelven actualizado.
"""

class StateStorageManager(metaclass=SingletonMeta):

    def __init__(self):
        initial_state = dict()
        STATE_STORAGE = dcc.Store(**{'id': 'StateStorage',
                                     'storage_type': 'session'},
                                  data=initial_state)
        self.__initial_state_storage = STATE_STORAGE
        self.__serie_base = {
            'Grafica': None,
            'Axis': None,
            'Style': None
        }
        return None

    def get_initial_state_storage(self):
        return self.__initial_state_storage

    def __add_selected_operation(self, op_id, state_storage):
        """
        Adds a new selected operation to the state storage.
        """
        state_storage[op_id] = {
            'Tabla': None,
            'VariableValor': dict(),
            'Serie': None
        }
        return state_storage

    def update_selected_operation(self,
                                  prev_op_id, current_op_id,
                                  state_storage):
        state_storage.pop(prev_op_id, None)
        state_storage = self.__add_selected_operation(current_op_id,
                                                      state_storage)
        return state_storage

    def __add_selected_table(self, op_id, tab_id, state_storage):
        state_storage[op_id]['Tabla'] = tab_id
        return state_storage

    def update_selected_table(self, op_id,
                              previous_tab_id, current_tab_id,
                              state_storage):
        return self.__add_selected_table(op_id, current_tab_id, state_storage)

    def __add_selected_variable(self, op_id, var_id, state_storage):
        state_storage[op_id]['VariableValor'][var_id] = None
        return state_storage

    def update_selected_variable(self, op_id,
                                 previous_var_id, current_var_id,
                                 state_storage):
        state_storage[op_id]['VariableValor'].pop(previous_var_id, None)
        state_storage = self.__add_selected_variable(op_id,
                                                     current_var_id,
                                                     state_storage)
        return state_storage

    def __add_selected_value(self, op_id, var_id, val_id, state_storage):
        state_storage[op_id]['VariableValor'][var_id] = val_id
        return state_storage

    def update_selected_value(self,
                              op_id,
                              var_id,
                              previous_val_id, current_val_id,
                              state_storage):

        return self.__add_selected_value(op_id, var_id,
                                         current_val_id, state_storage)

    def __add_selected_serie(self, op_id, serie_id, state_storage):
        state_storage[op_id]['Serie'][serie_id] = dict(self.__serie_base)
        # Wrapped around dict to make a copy
        return state_storage

    def update_selected_serie(self, op_id,
                              previous_serie_id, current_serie_id,
                              state_storage):
        state_storage[op_id]['Serie'].pop(previous_serie_id, None)
        return self.__add_selected_serie(op_id,
                                         current_serie_id, state_storage)

    def __add_selected_graph(self, op_id, serie_id, graph_id, state_storage):
        state_storage[op_id]['Serie'][serie_id]['Grafica'] = graph_id
        return state_storage

    def update_selected_graph(self,
                              op_id, serie_id,
                              previous_graph_id, current_graph_id,
                              state_storage):
        return self.__add_selected_graph(op_id, serie_id,
                                         current_graph_id,
                                         state_storage)

    def __add_selected_graph_axis(self, op_id, serie_id,
                                  axis,
                                  state_storage):
        state_storage[op_id]['Serie'][serie_id]['Axis'] = axis
        return state_storage

    def update_selected_graph_axis(self,
                                   op_id, serie_id,
                                   previous_axis, current_axis,
                                   state_storage):
        return self.__add_selected_graph_axis(op_id, serie_id,
                                              current_axis,
                                              state_storage)

    def __add_selected_graph_style(self,
                                   op_id, serie_id,
                                   style,
                                   state_storage):
        state_storage[op_id]['Serie'][serie_id]['Style'] = style
        return state_storage

    def update_selected_graph_style(self,
                              op_id, serie_id,
                              previous_style, current_style,
                              state_storage):
        return self.__add_selected_graph_style(op_id,
                                               serie_id,
                                               current_style,
                                               state_storage)






























