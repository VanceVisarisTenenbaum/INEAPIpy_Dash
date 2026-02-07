# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 18:32:31 2025

@author: mano
"""

from dash import html
from Components.UIComponents.Managers.UIManager import UIManager
from Components.UIComponents.Common.NewRowButton import NewRowButtonComp
from Components.UIComponents.Inputs.VariableComponent import VariableComponent
from Components.UIComponents.Inputs.ValorComponent import ValorComponent




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

UIM = UIManager()
def VarValPair(var_comp, val_comp, row_lv1, row_lv2):
    """Returns a well placed pair of var-values selects."""

    component = html.Div(
        children=[
            var_comp,
            html.Div('', className='svg left-right-arrow'),
            val_comp
        ],
        className='pair-item',
        **{'id': UIM.id_generator(ui_type='Arranger',
                                  ui_name='ParVariableValor',
                                  row_lv1=row_lv1,
                                  row_lv2=row_lv2)}
    )

    return component


def VarValPairBoxComponent(row_lv1, initial_varvalpair):
    """Caja con pares Variable-Valor separados en filas."""
    vvp = html.Div(
        children=[initial_varvalpair],
        **{'id': UIM.id_generator(ui_type='Arranger',
                                  ui_name='ParesVariableValor',
                                  row_lv1=row_lv1)},
        className='pairs-list'
    )
    component = html.Div(
        children=[vvp, NewRowButtonComp('ParesVariableValor', row_lv1)]
    )
    return component


def make_vvp(row_lv1, row_lv2, variables=list(), valores=list()):
    VarC = VariableComponent(row_lv1, row_lv2, variables)
    ValC = ValorComponent(row_lv1, row_lv2, valores)
    return VarValPair(VarC, ValC, row_lv1, row_lv2)


