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

from dash import callback, ctx, clientside_callback, ClientsideFunction

from Components.Storage.ServerMemory import ServerMemoryManager
from Components.Storage.RequestsStorage import RequestsStorageManager
from Components.Storage.StateStorage import StateStorageManager
from Components.Storage.DummyStorage import DummyStorageManager

from Components.UIComponents.Common.SelectComponent import SelectComponent
from Components.UIComponents.Common.ui_processes import (STORAGE_INPUTS,
                                                         STORAGE_OUTPUTS,
                                                         DUMMY_INPUT,
                                                         DUMMY_OUTPUT,
                                                         io_generator)


from Components.UIComponents.VariableComponent import (VariableComponent,
                                                       variable_event_listener_adder)
from Components.UIComponents.ValorComponent import ValorComponent
from Components.UIComponents.VarValPairsBox import (VarValPairBoxComponent,
                                                    VarValPair)
from Components.UIComponents.SelectionBox import InputsGroupRow
from Components.UIComponents.TableComponent import (TableSelectBox,
                                                    table_event_listener_adder)



DSM = DummyStorageManager()
SSM = StateStorageManager()
RSM = RequestsStorageManager()

def OperationSelectBox(row_lv1):
    SSM = ServerMemoryManager()
    return SelectComponent(SSM.get_metadata('Operaciones'), 'O', row_lv1)

"""
Cuando un usuario elige una operación ocurre lo siguiente:
    1- Se actualizan los valores del select de tabla y variable asociados.
    2- Se genera una nueva fila para la selección de Operacion.
"""

"""
El select de Operación tiene que tener un event listener para saber
cuando el usuario ha seleccionado una opearción.

Cuando esto ocurre, se ejecutan los siguientes pasos:
    1- Se guarda la seleccion en el estado.
    2- Se cargan las tablas asociadas.
    3- Se cargan las variables asociadas.
    4- Se añaden las tablas a las opciones del select.
    5- Se añaden las variables a las opciones del select.
    6- Se añaden los event listeners a ambos selects.
    7- Se genera una nueva fila para la selección de operación.
    8- Se añaden los event listeners al nuevo select de operacion.

Para cumplir esto, el input es:
    1- la operación elegida.
    2- el almacenamiento de peticiones.
    3- el almacenamiento de estado.
    4- Los hijos del contenedor padre.
    5- Las opciones actuales de tablas.
    6- Las opciones actuales de Variable.
    7- La opción actual de operación.
    8- El almacenamiento dummy.

Las salidas deben ser:
    1- Las opciones del select de tabla asociado.
    2- Las opciones del select de variable asociado.
    3- El almacenamiento de peticiones
    4- El almacenamiento de estado.
    5- Los hijos del contenedor padre con el nuevo hijo añadido.
"""

def make_vvp(row_lv1, row_lv2):
    VrC = VariableComponent(row_lv1, row_lv2, list())
    VlC = ValorComponent(row_lv1, row_lv2, list())
    return VarValPair(VrC, VlC, row_lv1, row_lv2)

def update_state_storage(row_lv1,
                         prev_op_id, current_op_id,
                         state_storage):
    state_storage = SSM.update_selected_operation(row_lv1,
                                                  prev_op_id, current_op_id,
                                                  state_storage)
    return state_storage

def get_tables(op_id, requests_storage):
    return RSM.get_obj('Tabla', op_id, requests_storage)

def get_variables(op_id, requests_storage):
    return RSM.get_obj('Variable', op_id, requests_storage)


def add_new_row_event_listeners(row_lv1):
    operation_event_listener_adder(row_lv1 + 1)
    return None

def make_row(row_lv1):
    NewRow = InputsGroupRow(row_lv1,
                            OperationSelectBox(row_lv1),
                            TableSelectBox(row_lv1,list()),
                            VarValPairBoxComponent(row_lv1,
                                                   make_vvp(row_lv1,
                                                            1)))

    return NewRow



def server_event_listeners():
    """Adds the event listener to the operation box."""

    #step1_name = DSM.namer('O', row_lv1)
    #step2_name = DSM.namer('O2', row_lv1)


    def prev_checks(selected_op_id, state_storage, row_lv1):
        if selected_op_id is None:
            return False, None
        prev_op_id = SSM.get_current_value(row_lv1, None,
                                           'Operacion', state_storage)
        if prev_op_id == selected_op_id:
            return False, None
        return True, prev_op_id




    @callback(
        *STORAGE_OUTPUTS()[:2],  # Request y State
        DUMMY_OUTPUT(allow_duplicate=True),
        io_generator('Input', 'O', None, 'ALL', None, 'value'),
        *STORAGE_INPUTS()[:2],  # Request y State
        DUMMY_INPUT(state=True),
        prevent_initial_call=True
    )
    def process(selected_op_id, requests_storage, state_storage, dummy_storage):

        row_lv1 = ctx.triggered_id['fila_lv1']
        selected_op_id = ctx.triggered[0]['value']
        checks, prev_op_id = prev_checks(selected_op_id, state_storage,
                                         row_lv1)
        if not checks:
            return requests_storage, state_storage, dummy_storage
        # Los pasos son:
        # 1- Actualizar el estado.
        state_storage = update_state_storage(row_lv1,
                                             prev_op_id,
                                             selected_op_id,
                                             state_storage)
        # 2- Obtener las tablas y variables
        # Obtenemos las tablas
        tablas, requests_storage = get_tables(selected_op_id,
                                              requests_storage)
        # Obtenemos las variables
        variables, requests_storage = get_variables(selected_op_id,
                                                    requests_storage)

        # Actualizamos el dummy
        dummy_storage = DSM.set_random_number(dummy_storage)


        return requests_storage, state_storage, dummy_storage

    table_event_listener_adder()
    variable_event_listener_adder()


    return None


def client_event_listeners():
    # Add new row client callback
    clientside_callback(
        ClientsideFunction(
            namespace='clientside',
            function_name='add_new_op_row'
        ),
        io_generator('Output', 'ISB', None, None, None, 'children'),
        io_generator('Input', 'O', 'Boton', None, None, 'n_clicks'),
        io_generator('State', 'ISB', None, None, None, 'children'),
        STORAGE_INPUTS()[0]  # Request
    )

    # Add options to table
    clientside_callback(
        ClientsideFunction(
            namespace='clientside',
            function_name='add_options_to_input_table'
        ),
        io_generator('Output', 'T', None, 'MATCH', None, 'options'),
        DUMMY_INPUT(),
        io_generator('State', 'O', None, 'MATCH', None, 'value'),
        STORAGE_INPUTS()[0]  # Requests
    )

    # Add options to variable
    clientside_callback(
        ClientsideFunction(
            namespace='clientside',
            function_name='add_options_to_input_variable'
        ),
        io_generator('Output', 'Vr', None, 'MATCH', None, 'options'),
        DUMMY_INPUT(),
        io_generator('State', 'O', None, 'MATCH', None, 'value'),
        STORAGE_INPUTS()[0]  # Requests
    )

    return None


def operation_event_listener_adder():
    server_event_listeners()
    client_event_listeners()
    return None




