# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 18:32:31 2025

@author: mano
"""

from dash import html, dcc
#from .SharedFunctions import INE

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
    options = [{'label': '', 'value': 'None'}]
    options.extend(list_of_labels_values)

    # Adds initial empty value
    component = dcc.Dropdown(
        options=options,
        value='None',  # Default value
        **{'id': str(name) + 'Select_' + str(op_id) + '_' + str(row_number)},
        style={
            'width': '250px',
            'height': '50px',
            'padding': '6px'
        }
    )
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


# BORRAR CUANDO YA NO SE USE

sample = [
    {'label': 'test ' + str(i), 'value': i}
    for i in range(10)
]

childrens_sample = [
    VarValPair(
        SelectComponent(sample, 'Var', 1, i),
        SelectComponent(sample, 'Val', 1, i),
        1, i
    )
    for i in range(10)
]

# FIN DE LO QUE HAY QUE BORRAR

def VarValPairBoxComponent(op_id):
    """Caja con pares Variable-Valor separados en filas."""
    component = html.Div(
        children=childrens_sample,
        **{'id': 'VarValBox' + str(op_id)},
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

def make_variables_select(op_id):
    return None
