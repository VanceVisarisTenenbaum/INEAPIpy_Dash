# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 18:32:31 2025

@author: mano
"""

from dash import html, dcc, Input, Output, State, callback
from .SharedFunctions import (LabelInput,
                              SELECT_INPUT_STYLE,
                              check_if_loaded,
                              extract_labels_values)
from .ServerMemory import ServerMemoryManager

"""
This file contains a fuction that creates a Component that will allow the user
to select multiple pairs Variable-Valor.

The Component starts with just one pair of select options and will add more
if the user selects the available pairs.

For example, starts with one empty Pair, if the user selects a Variable and a
Valor, then it adds a new empty pair.

Since the Variables and Valores depend on the selected operation, the op_id
becomes a param.
"""

# Row_number hace referencia al número de fila del par variable valor
# no al de selección de operación.

def SelectComponent(list_of_labels_values, name, op_id, row_number):
    """Returns a select for variables or values."""

    # Adds initial empty value
    InputComponent = dcc.Dropdown(
        options=list_of_labels_values,
        value=None,  # Default value is empty
        **{'id': str(name) + 'Select_' + str(op_id) + '_' + str(row_number)},
        style=SELECT_INPUT_STYLE
    )

    component = LabelInput(name, InputComponent, 'top')
    return component


def VarValPair(var_comp, val_comp, op_id, row_number):
    """Returns a well placed pair of var-values selects."""
    component = html.Div(
        children=[var_comp, val_comp],
        style={
            "display": "flex",
            "flexDirection": "row",
            "justifyContent": "center",
            "gap": "12px",  # Espacio fijo mínimo entre ellos
            "width": "100%"
        },
        **{'id': 'VarValPair_' + str(op_id) + '_' + str(row_number)}
    )
    return component


def VarValPairBoxComponent(op_id, row_number):
    """Caja con pares Variable-Valor separados en filas."""
    component = html.Div(
        children=[],
        **{'id': 'VarValBox_' + str(op_id) + '_' + str(row_number)},
        style={
            "display": "flex",
            "flexDirection": "column",
            "overflowY": "auto",        # Scroll vertical si hay overflow
            "maxHeight": "300px",       # Altura máxima fija del contenedor
            "width": "100%",
            "border": "1px solid #ccc",
            "padding": "10px"
        }
    )
    return component


#
#
#
#
# Añadimos los event listeners

# Primero necesitamos un event listener que obtenga los valores según la
# variable solicitada.

def add_values_to_storage(var_id, session_storage):
    if isinstance(var_id, int):
        if check_if_loaded(var_id, 'Variable', session_storage):
            return session_storage
        SMM = ServerMemoryManager()
        valores = SMM.INE.get_values_(var_id)

        session_storage['Valores'][var_id] = valores
        session_storage['VariablesSolicitadas'].add(var_id)
    return session_storage


def get_variables_from_storage(op_id, session_storage):
    return session_storage['Variables'][op_id]


def get_values_from_storage(var_id, session_storage):
    add_values_to_storage(var_id, session_storage)
    return session_storage['Valores'][var_id]


def make_new_varval_row(op_id, row_number, session_storage, state_storage):

    selected_vars = [
        varval['variable'] for varval in state_storage[op_id]['VariableValor']
    ]

    variables = get_variables_from_storage(op_id, session_storage)
    variables = [v for v in variables if v['Id'] not in selected_vars]

    VarSel = SelectComponent(extract_labels_values(variables),
                             'Var',
                             op_id,
                             row_number)
    ValSel = SelectComponent([], 'Val', op_id, row_number)

    # Cuando creas una nueva fila, es necesario añadirle los event listeners
    # a cada input.
    varval_event_listener_adder(op_id, row_number)

    return VarValPair(VarSel, ValSel, op_id, row_number)


def add_variable_to_state_storage(op_id, var_id, state_storage):
    state_storage[op_id]['VariableValor'][var_id] = None
    return state_storage


def add_value_to_state_storage(op_id, var_id, val_id, state_storage):
    state_storage[op_id]['VariableValor'][var_id] = val_id
    return state_storage





def varval_event_listener_adder(op_id, row_number):

    @callback(
        Output('SessionStorage', 'data'),
        Output('StateStorage', 'data'),
        Output('ValSelect_' + str(op_id) + '_' + str(row_number), 'value'),
        Output('VarValBox_' + str(op_id) + '_' + str(row_number), 'children'),
        Input('VarSelect_' + str(op_id) + '_' + str(row_number), 'value'),
        State('SessionStorage', 'data'),
        State('StateStorage', 'data'),
        State('VarValBox_' + str(op_id) + '_' + str(row_number), 'children')
    )
    def variable_selection_steps(var_id,
                                 session_storage, state_storage,
                                 VVPBoxContainerChildrens):
        # 1- Load the data to storage
        session_storage = add_values_to_storage(var_id)
        # 2- Load the values to the ValueSelect
        valores = get_values_from_storage(var_id, session_storage)
        # 3- Make a new VarValPair
        VVP = make_new_varval_row(op_id,
                                  row_number + 1,
                                  session_storage,
                                  state_storage)
        # 4- Add new VVP to the containerBox
        VVPBoxContainerChildrens.append(VVP)
        # 5- Add the selected variable to the StateStorage
        state_storage = add_variable_to_state_storage(op_id, var_id,
                                                      state_storage)

        return session_storage, state_storage, valores, VVPBoxContainerChildrens

    @callback(
        Output('SessionStorage','data'),
        State('VarSelect_' + str(op_id) + '_' + str(row_number), 'value'),
        Input('ValSelect_' + str(op_id) + '_' + str(row_number), 'value'),
        State('StateStorage', 'data'),
    )

    return None


