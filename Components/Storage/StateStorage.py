# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 11:42:49 2025

@author: mano
"""

from dash import dcc
from Components.Storage.SingletonCustom import SingletonMeta
from Components.UIComponents.Managers.UIManager import UIManager

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

UIM = UIManager()
class StateStorageManager(metaclass=SingletonMeta):

    def __init__(self):
        initial_state = dict()
        STATE_STORAGE = dcc.Store(**{'id': UIM.id_generator(
                                        ui_type='Storage',
                                        ui_name='State'
                                    ),
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

    def __add_selected_operation(self, row_lv1, op_id, state_storage):
        """
        Adds a new selected operation to the state storage.
        """
        state_storage[row_lv1] = {
            'Operacion': op_id,
            'Tabla': None,
            'VariableValor': dict(),
            'Serie': dict(),
        }
        return state_storage

    def update_selected_operation(self, row_lv1,
                                  prev_op_id, current_op_id,
                                  state_storage):
        state_storage = self.__add_selected_operation(row_lv1,
                                                      current_op_id,
                                                      state_storage)
        return state_storage

    def __add_selected_table(self, row_lv1, tab_id, state_storage):
        state_storage[row_lv1]['Tabla'] = tab_id
        return state_storage

    def update_selected_table(self, row_lv1,
                              previous_tab_id, current_tab_id,
                              state_storage):
        return self.__add_selected_table(row_lv1,
                                         current_tab_id, state_storage)

    def __add_selected_variable(self, row_lv1, row_lv2,  var_id, state_storage):
        state_storage[row_lv1]['VariableValor'][row_lv2] = {
            'Variable': var_id,
            'Valor': None
        }
        return state_storage

    def update_selected_variable(self, row_lv1, row_lv2,
                                 previous_var_id, current_var_id,
                                 state_storage):
        state_storage = self.__add_selected_variable(row_lv1,
                                                     current_var_id,
                                                     state_storage)
        return state_storage

    def __add_selected_value(self, row_lv1, row_lv2,
                             val_id, state_storage):
        state_storage[row_lv1]['VariableValor'][row_lv2]['Valor'] = val_id
        return state_storage

    def update_selected_value(self,
                              row_lv1, row_lv2,
                              previous_val_id, current_val_id,
                              state_storage):

        return self.__add_selected_value(row_lv1, row_lv2,
                                         current_val_id, state_storage)

    def __add_selected_serie(self, row_lv1, serie_id, state_storage):
        state_storage[row_lv1]['Serie'][serie_id] = dict(self.__serie_base)
        # Wrapped around dict to make a copy
        return state_storage

    def update_selected_serie(self, row_lv1,
                              previous_serie_id, current_serie_id,
                              state_storage):
        state_storage[row_lv1]['Serie'].pop(previous_serie_id, None)
        return self.__add_selected_serie(row_lv1,
                                         current_serie_id, state_storage)

    def __add_selected_graph(self, row_lv1, serie_id, graph_id, state_storage):
        state_storage[row_lv1]['Serie'][serie_id]['Grafica'] = graph_id
        return state_storage

    def update_selected_graph(self,
                              row_lv1, serie_id,
                              previous_graph_id, current_graph_id,
                              state_storage):
        return self.__add_selected_graph(row_lv1, serie_id,
                                         current_graph_id,
                                         state_storage)

    def __add_selected_graph_axis(self, row_lv1, serie_id,
                                  axis,
                                  state_storage):
        state_storage[row_lv1]['Serie'][serie_id]['Axis'] = axis
        return state_storage

    def update_selected_graph_axis(self,
                                   row_lv1, serie_id,
                                   previous_axis, current_axis,
                                   state_storage):
        return self.__add_selected_graph_axis(row_lv1, serie_id,
                                              current_axis,
                                              state_storage)

    def __add_selected_graph_style(self,
                                   row_lv1, serie_id,
                                   style,
                                   state_storage):
        state_storage[row_lv1]['Serie'][serie_id]['Style'] = style
        return state_storage

    def update_selected_graph_style(self,
                              row_lv1, serie_id,
                              previous_style, current_style,
                              state_storage):
        return self.__add_selected_graph_style(row_lv1,
                                               serie_id,
                                               current_style,
                                               state_storage)

    def get_current_value(self, row_lv1, row_lv2, name, state_storage):
        lv1 = state_storage.get(row_lv1, None)
        if lv1 is None:
            return None

        if name in ['Operacion', 'Tabla']:
            return lv1.get(name)
        elif name in ['Variable', 'Valor']:
            lv2 = lv1.get('VariableValor').get(row_lv2, None)
            if lv2 is None:
                return None
            return lv2.get(name)
        elif name == 'Serie':
            return state_storage[row_lv1]['Serie'].keys()
        else:
            raise ValueError(
                'name can only be {Operacion, Tabla, Variable, Valor, Serie}')
        return None






























