# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 18:32:31 2025

@author: mano
"""

from dash import html
from Components.UIComponents.Common.id_generator import id_generator_mapper
from Components.UIComponents.Common.Styles import (ROW_SEPARATED_DIVS,
                                                   COLUMN_SEPARATED_DIVS)


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


def VarValPair(var_comp, val_comp, row_lv1, row_lv2):
    """Returns a well placed pair of var-values selects."""
    component = html.Div(
        children=[var_comp, val_comp],
        style=COLUMN_SEPARATED_DIVS,
        **{'id': id_generator_mapper('VariableValor', None, row_lv1, row_lv2)}
    )
    return component


def VarValPairBoxComponent(row_lv1):
    """Caja con pares Variable-Valor separados en filas."""
    component = html.Div(
        children=[],
        **{'id': id_generator_mapper('VariableValor', 'Box',
                                     row_lv1)},
        style=ROW_SEPARATED_DIVS
    )
    return component




