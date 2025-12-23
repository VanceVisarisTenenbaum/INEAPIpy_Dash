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

from dash import callback, ctx, Patch

from Components.Storage.ServerMemory import ServerMemoryManager
from Components.Storage.RequestsStorage import RequestsStorageManager
from Components.Storage.StateStorage import StateStorageManager
from Components.Storage.DummyStorage import DummyStorageManager

from Components.UIComponents.Common.SelectComponent import SelectComponent
from Components.UIComponents.Common.ui_processes import (STORAGE_INPUTS,
                                                         STORAGE_OUTPUTS,
                                                         io_generator)


from Components.UIComponents.VariableComponent import (VariableComponent,
                                                       variable_event_listener_adder)
from Components.UIComponents.ValorComponent import ValorComponent
from Components.UIComponents.VarValPairsBox import (VarValPairBoxComponent,
                                                    VarValPair)
from Components.UIComponents.SelectionBox import InputsGroupRow
from Components.UIComponents.TableComponent import (TableSelectBox,
                                                    table_event_listener_adder)

from Components.SharedFunctions import extract_labels_values


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



def operation_event_listener_adder():
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
        io_generator('Output', 'ISB', None, None, None, 'children'),
        io_generator('Output', 'T', None, 'MATCH', None, 'options'),
        io_generator('Output', 'Vr', None, 'MATCH', None, 'options'),
        *STORAGE_OUTPUTS()[:2],  # Request y State
        io_generator('Input', 'O', None, 'MATCH', None, 'value'),
        io_generator('State', 'T', None, 'MATCH', None, 'options'),
        io_generator('State', 'Vr', None, 'MATCH', None, 'options'),
        io_generator('State', 'ISB', None, None, None, 'children'),
        *STORAGE_INPUTS()[:2],  # Request y State
        prevent_initial_call=True
    )
    def process(selected_op_id,
                table_current_options, variable_current_options,
                parent_childrens,
                requests_storage, state_storage):

        row_lv1 = ctx.triggered_id['fila_lv1']
        checks, prev_op_id = prev_checks(selected_op_id, state_storage,
                                         row_lv1)
        if not checks:
            return (parent_childrens,
                    table_current_options, variable_current_options,
                    requests_storage, state_storage)
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
        tablas = extract_labels_values(tablas)
        variables = extract_labels_values(variables)

        # 3-  Creamos la nueva fila
        ISBPatch = Patch()
        ISBPatch.append(make_row(row_lv1 + 1))


        return ISBPatch, tablas, variables, requests_storage, state_storage

    table_event_listener_adder(1)
    variable_event_listener_adder()


    """
    @callback(
        Output(id_generator_mapper('T', None, row_lv1), 'options'),
        Output(id_generator_mapper('Vr', None, row_lv1, 1), 'options'),
        *STORAGE_OUTPUTS(),
        Input(id_generator_mapper('O', None, row_lv1), 'value'),
        *STORAGE_INPUTS(),
        State(id_generator_mapper('T', None, row_lv1), 'options'),
        State(id_generator_mapper('Vr', None, row_lv1, 1), 'options'),
        prevent_initial_call=True
    )
    def step_1(selected_op_id,
               requests_storage,
               state_storage,
               dummy_storage,
               table_current_options,
               variable_current_options
               ):
        print('Step 1')
        # Comprobamos si la función tiene que ejecutarse o no
        checks, prev_op_id = prev_checks(selected_op_id, state_storage)
        if not checks:
            return (table_current_options, variable_current_options,
                    requests_storage, state_storage, dummy_storage)

        # En la primera ejecución actualizamos el estado
        # y las tablas y variables
        if DSM.get_last_update(dummy_storage) == DSM.get_default_value():
            # actualizamos el estado
            state_storage = update_state_storage(row_lv1,
                                                 prev_op_id,
                                                 selected_op_id,
                                                 state_storage)
            # Obtenemos las tablas
            tablas, requests_storage = get_tables(selected_op_id,
                                                  requests_storage)
            # Obtenemos las variables
            variables, requests_storage = get_variables(selected_op_id,
                                                        requests_storage)

            tablas = extract_labels_values(tablas)
            variables = extract_labels_values(variables)
            # Como ya existen en el layout, añadimos los event listeners.
            table_event_listener_adder(row_lv1)
            variable_event_listener_adder(row_lv1, 1)

            # Actualizamos el dummy
            dummy_storage = DSM.add_update(step1_name, dummy_storage)
            return (tablas, variables,
                    requests_storage, state_storage, dummy_storage)

        # Return por defecto.
        return (table_current_options, variable_current_options,
                requests_storage, state_storage, dummy_storage)

    @callback(
        Output('ISB', 'children'),
        STORAGE_OUTPUTS([True, True, False])[2], # Dummy
        State(id_generator_mapper('O', None, row_lv1), 'value'),
        State('ISB', 'children'),
        *STORAGE_INPUTS()[1:3], # State and dummy
        prevent_initial_call=True
    )
    def step_2(selected_op_id,
               parent_childrens,
               state_storage,
               dummy_storage
               ):
        print('Step 2')
        checks, prev_op_id = prev_checks(selected_op_id, state_storage)
        if not checks:
            return parent_childrens, dummy_storage
        # Se vuelve a ejecutar la función, ahora este segundo paso.
        # Añadimos la nueva fila.
        if DSM.get_last_update(dummy_storage) == step1_name:
            # creamos la nueva fila
            new_row = make_row(row_lv1 + 1)
            # Lo añadimos a los hijos del padre
            parent_childrens = add_new_son(parent_childrens, new_row)
            # Actualizamos el dummy
            dummy_storage = DSM.add_update(step2_name, dummy_storage)

        return parent_childrens, dummy_storage

    @callback(
        STORAGE_OUTPUTS()[2],  # dummy
        State(id_generator_mapper('O', None, row_lv1), 'value'),
        *STORAGE_INPUTS()[1:3], # State and dummy
        prevent_initial_call=True
    )
    def step_3(selected_op_id,
               state_storage,
               dummy_storage):
        print('Step 3')
        checks, prev_op_id = prev_checks(selected_op_id, state_storage)
        if not checks:
            return dummy_storage

        # Ahora que ya se ha añadido una nueva fila, añadimos los
        # event listeners.
        if DSM.get_last_update(dummy_storage) == step2_name:
            # Añadimos el event listener a la nueva operacion.
            operation_event_listener_adder(row_lv1 + 1)
            # Actualizamos el dummy
            dummy_storage = DSM.reset_default_value(dummy_storage)

        return dummy_storage
    """

    return None


