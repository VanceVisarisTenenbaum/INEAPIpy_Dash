# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 13:34:22 2025

@author: mano
"""

from dash import callback, ctx, Patch

from Components.UIComponents.Common.SelectComponent import SelectComponent
from Components.UIComponents.Common.ui_processes import (add_new_son,
                                                         remove_sons,
                                                         STORAGE_INPUTS,
                                                         STORAGE_OUTPUTS,
                                                         io_generator)

from Components.UIComponents.VarValPairsBox import VarValPair
from Components.UIComponents.ValorComponent import (ValorComponent,
                                                    valor_event_listener_adder)

from Components.Storage.RequestsStorage import RequestsStorageManager
from Components.Storage.StateStorage import StateStorageManager
from Components.Storage.DummyStorage import DummyStorageManager

def VariableComponent(row_lv1, row_lv2, list_of_ine_vars):
    component = SelectComponent(list_of_ine_vars, 'Vr', row_lv1, row_lv2)
    return component


"""
Cuando el usuario selecciona una variable ocurre lo siguiente:
    1- Se cargan los valores asociados a dicha variable.
    2- Se actualizan los valores del select de valores asociado.
    3- Se actualiza el estado de la app.
    4- Se añade una nueva fila para la selección de variables.

Para conseguir esto los inputs son:
    1- La Operación elegida previamente.
    2- La variable elegida.
    3- el almacenamiento de peticiones.
    4- el almacenamiento de estado.
    5- los hijos del contenedor padre.

Las salidas son:
    1- Las opciones del select de valor asociado.
    2- El almacenamiento de peticiones.
    3- El almacenamiento de estado.
    4- Las hijos del contenedor padre.
"""
DSM = DummyStorageManager()
SSM = StateStorageManager()
RSM = RequestsStorageManager()

def make_var_val_comp(op_id, row_lv1, row_lv2, session_storage):
    variables, session_storage = RSM.get_obj('Variable',
                                              op_id,
                                              session_storage)
    VrC = VariableComponent(row_lv1, row_lv2, variables)
    VlC = ValorComponent(row_lv1, row_lv2, list())
    return VarValPair(VrC, VlC, row_lv1, row_lv2)


def add_new_row_process(current_childrens, new_row, row_lv2):
    """
    Makes new varval pair row.

    En este caso, dado que los sucesivas filas dependen de las anteriores
    tenemos que eliminarlas y añadir una nueva.
    """
    current_childrens = remove_sons(current_childrens, row_lv2)
    current_childrens = add_new_son(current_childrens, new_row)
    return current_childrens

def update_state_storage(row_lv1, row_lv2,
                         previous_var_id, current_var_id,
                         state_storage):
    state_storage = SSM.update_selected_variable(row_lv1, row_lv2,
                                                 previous_var_id,
                                                 current_var_id, state_storage)
    return state_storage

def get_valor_values(var_id, requests_storage):
    valores, requests_storage = RSM.get_obj('Valor', var_id, requests_storage)
    return valores, requests_storage

def update_dummy(dummy_name, dummy_storage):
    return DSM.add_update(dummy_name, dummy_storage)

def add_new_row_event_listeners(row_lv1, row_lv2):
    variable_event_listener_adder(row_lv1, row_lv2 + 1)
    valor_event_listener_adder(row_lv1, row_lv2 + 1)
    return None



"""
Las funciones anteriores incluyen todos los procesos que tienen que ocurrir
al seleccionar una variable.

1- Se actualiza el Storage de Estado.
2- Se actualizan las opciones del valor asociado.
3- Se añade la nueva fila.
4- Se añade los event listeners a la nueva fila.

Para añadir una nueva fila es necesario obtener los hijos del padre,
añadirle uno nuevo y devolver los hijos del padre y esto no se puede hacer
en una única ejecución, por que tomar los hijos del padre en la primera
ejecución no contienen las opciones que se van a añadir, y al devolverlo
se han eliminado las opciones que se introdujeron inicialmente, por este
motivo es necesario ejecutarlo una vez se han actualizado los valores.

Lo mismo ocurre con los event listeners, estos no funcionan si los objetos
no están en el layout, por eso se deben añadir tras añadir la nueva fila.

Para este propósito se utiliza el DummyStorage, para almacenar qué fue lo
último que se ejecutó.
"""

"""
Para definir los Outputs, los Inputs y State Ids:
    Dependencias:
        1- Operation Select Value
        2- Session Storage data
        3- Previous Selected Var Value
        4- Current Selected Var Value
        5- State Storage data
        6- Dummy Storage data
        7- Current Parent Childrens
        8- Current Valor Options
    Resultados
        1- Valor Select Options
        2- Updated Parent Childrens
        3- Updated Session Storage
        4- Updated State Storage
        5- Updated Dummy Storage

"""




def variable_event_listener_adder():
    """Adds the event listener to the Variable Select."""
    #step1_name = DSM.namer('Vr', row_lv1)
    #step2_name = DSM.namer('Vr2', row_lv1)
    #print('Var Event')

    def prev_checks(selected_var_id, state_storage, row_lv1, row_lv2):
        if selected_var_id is None:
            # Para el caso de la ejecución inicial o si no se selecciona
            # ninguna variable
            return False, None
        # Al usar el con Input, cualquier proceso que lo actualice forzará
        # la ejecución de esta función, por eso debemos comprobar si ha
        # cambiado el valor del input de la variable para ejecutar esta
        # todo el proceso.
        prev_var_id = SSM.get_current_value(row_lv1, row_lv2,
                                            'Variable', state_storage)
        if selected_var_id == prev_var_id:
            return False, None
        return True, prev_var_id


    @callback(
        io_generator('Output', 'VariableValor', 'Box', 'MATCH', None,
                     'children'),
        io_generator('Output', 'Vl', None, 'MATCH', 'MATCH', 'options'),
        *STORAGE_OUTPUTS()[:2],  # Requests and State
        io_generator('State', 'O', None, 'MATCH', None, 'value'),
        io_generator('Input', 'Vr', None, 'MATCH', 'MATCH', 'value'),
        io_generator('State', 'VariableValor', 'Box', 'MATCH', None,
                     'children'),
        io_generator('State', 'Vl', None, 'MATCH', 'MATCH', 'options'),
        *STORAGE_INPUTS()[:2],  # Requests and State
        prevent_initial_call=True
    )
    def process(op_id, selected_var_id, parent_children, current_valor_options,
                requests_storage, state_storage):

        row_lv1 = ctx.triggered_id['fila_lv1']
        row_lv2 = ctx.triggered_id['fila_lv2']
        checks, prev_var_id = prev_checks(selected_var_id, state_storage)
        if not checks:
            return (parent_children, current_valor_options,
                    requests_storage, state_storage)

        # 1- Actualizamos el estado.
        state_storage = update_state_storage(row_lv1, row_lv2,
                                             prev_var_id,
                                             selected_var_id,
                                             state_storage)
        # 2- Obtenemos los valores.
        valores, requests_storage = get_valor_values(selected_var_id,
                                                     requests_storage)

        # 3- Añadimos una nueva fila.
        newVVP = make_var_val_comp(op_id,
                                   row_lv1, row_lv2 + 1,
                                   requests_storage)
        VVPBoxPatch = Patch()
        # Añadimos el hijo
        VVPBoxPatch.append(newVVP)


        return VVPBoxPatch, valores, requests_storage, state_storage

    valor_event_listener_adder()

    """

    @callback(
        Output(id_generator_mapper('Vl'), 'options'),
        *STORAGE_OUTPUTS(),
        # --------------------------- Inputs
        State(id_generator_mapper('O', None, row_lv1), 'value'),
        Input(id_generator_mapper('Vr', None, row_lv1, row_lv2), 'value'),
        *STORAGE_INPUTS(),
        State(id_generator_mapper('Vl', None, row_lv1, row_lv2), 'options'),
        prevent_initial_call=True
    )
    def step_1(op_id,
               selected_var_id,
               requests_storage, state_storage,
               dummy_storage,
               current_valor_options):
        print('Step 1 Var')
        checks, prev_var_id = prev_checks(selected_var_id, state_storage)
        if not checks:
            return (current_valor_options,
                    requests_storage, state_storage, dummy_storage)

        # Definimos el primer paso.
        # El valor del dummy debería ser el valor
        # por defecto cuando se han terminado todos los procesos.
        # Y se puede ejecutar el primer paso.
        if DSM.get_last_update(dummy_storage) == DSM.get_default_value():
            # Actualizamos el estado
            state_storage = update_state_storage(row_lv1, row_lv2,
                                                 prev_var_id,
                                                 selected_var_id,
                                                 state_storage)
            # Obtenemos los valores
            valores, requests_storage = get_valor_values(selected_var_id,
                                                         requests_storage)
            # Actualizamos el dummy
            dummy_storage = update_dummy(step1_name, dummy_storage)
            return (valores,
                    requests_storage, state_storage, dummy_storage)

        # Por defecto por si acaso.
        return (current_valor_options,
                requests_storage, state_storage, dummy_storage)

    @callback(
        Output(id_generator_mapper('VariableValor', 'Box', row_lv1),
               'children'),
        STORAGE_OUTPUTS()[2],  # dummy
        State(id_generator_mapper('O', None, row_lv1), 'value'),
        State(id_generator_mapper('Vr', None, row_lv1, row_lv2), 'value'),
        State(id_generator_mapper('VariableValor', 'Box', row_lv1),
               'children'),
        *STORAGE_INPUTS(),
        prevent_initial_call=True
    )
    def step_2(op_id,
               selected_var_id,
               parent_childrens,
               requests_storage, state_storage, dummy_storage):

        print('Step 2 Var')
        checks, prev_var_id = prev_checks(selected_var_id, state_storage)
        if not checks:
            return parent_childrens, dummy_storage

        # Una vez se completa la función con el paso anterior, se ha
        # actualizado el dummy y se vuelve a ejecutar esta función, ya que
        # el dummy es un Input y esto hace que esta función se ejecute con
        # cada actualización del dummy.
        if DSM.get_last_update(dummy_storage) == step1_name:
            # Creamos la nueva fila.
            newVVP = make_var_val_comp(op_id,
                                       row_lv1, row_lv2 + 1,
                                       requests_storage)
            # Añadimos la nueva fila al padre.
            parent_childrens = add_new_row_process(parent_childrens,
                                                   newVVP, row_lv2)
            # Actualizamos el dummy
            dummy_storage = update_dummy(step2_name, dummy_storage)

        return parent_childrens, dummy_storage

    @callback(
        STORAGE_OUTPUTS()[2],  # dummy
        State(id_generator_mapper('Vr', None, row_lv1, row_lv2), 'value'),
        *STORAGE_INPUTS()[1:3],  # state y dummy
        prevent_initial_call=True
    )
    def step_3(selected_var_id,
               state_storage, dummy_storage):
        print('Step 3 Var')
        checks, prev_var_id = prev_checks(selected_var_id, state_storage)
        if not checks:
            return dummy_storage

        # En este punto ya debería existir la nueva fila en el layout
        # y podemos añadir los event listeners.

        if DSM.get_last_update(dummy_storage) == step2_name:
            add_new_row_event_listeners(row_lv1, row_lv1)
            dummy_storage = DSM.reset_default_value(dummy_storage)

        return dummy_storage
    """


    return None