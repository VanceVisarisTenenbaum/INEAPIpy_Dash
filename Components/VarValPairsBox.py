# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 18:32:31 2025

@author: mano
"""

from dash import html, dcc, Input, Output, State, callback
from .SharedFunctions import LabelInput, SELECT_INPUT_STYLE

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
        **{'id': 'VarValBox' + str(op_id) + '_' + str(row_number)},
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

def variable_event_listener_adder(op_id, row_number):

    def add_values_to_storage():
        return None

    return None

# También hay que añadir un event listener que añade una nueva fila para
# la selección de nuevas variables.
