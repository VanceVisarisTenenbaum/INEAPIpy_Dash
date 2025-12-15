# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 22:25:24 2025

@author: mano
"""

"""
This file contains the function that creates a select for one Operation,
with two additional optional selects, Periodicity and Classification.
"""

from dash import dcc, Input, Output, State, callback
from .SharedFunctions import (LabelInput,
                              SELECT_INPUT_STYLE,
                              extract_labels_values,
                              check_if_loaded)
from .ServerMemory import ServerMemoryManager


def OperationSelectBox(row_number):

    SERVER_MEMORY = ServerMemoryManager().get_server_memory()


    options = [
        extract_labels_values(op)
        for op in SERVER_MEMORY['Operaciones']
    ]
    InputComponent = dcc.Dropdown(
        options=options,
        value=None,  # Default value is empty
        **{'id': 'OpSelect_' + str(row_number)},
        style=SELECT_INPUT_STYLE
    )

    component = LabelInput('Operaciones', InputComponent)
    return component

"""
Asociado con la operación, una vez se selecciona la operación es necesario
adquirir las tablas y las variables asociadas.

Definimos un event listener que al seleccionar una operación se carguen
las tablas y las variables.

Cómo es posible tener múltiples selecciones de operaciones, es necesario
hacer una función que añada el event listener a cada caja.
"""

def operation_event_listener_adder(row_number):

    @callback(
        Output('SessionStorage', 'data'),
        Input('OpSelect_' + str(row_number), 'value'),
        State('SessionStorage', 'data')
    )
    def add_tables_and_vars_to_storage(op_id, session_storage):
        if isinstance(op_id, int):
            if check_if_loaded(op_id, 'Operacion', session_storage):
                return session_storage
            SMM = ServerMemoryManager()
            tablas = SMM.INE.get_tables_(op_id)
            variables = SMM.INE.get_variables_(op_id)

            session_storage['Tablas'][op_id] = tablas
            session_storage['Variables'][op_id] = variables
            session_storage['OperacionesSolicitadas'].add(op_id)

        return session_storage
    return None


# Hay que añadir un event listener que al seleccionar una operación añada
# la seleccion de tabla y seleccion de variables valor.