# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 18:23:10 2025

@author: mano
"""

"""
This files contains a function that creates a box that will allow to select
everything necessary to get a set of series.
"""

from dash import html
from Components.UIComponents.Managers.UIManager import UIManager
from Components.UIComponents.Common.NewRowButton import NewRowButtonComp
from Components.UIComponents.Inputs.OperationComponent import OperationSelectBox
from Components.UIComponents.Inputs.TableComponent import TableSelectBox
from Components.UIComponents.Arrangers.VarValPairsBox import make_vvp

UIM = UIManager()

def InputsGroupRow(row_lv1, op_comp, tab_comp, varvalbox_comp):
    """
    This box provides the next.
        - Operation Selection
            * Periodicity Selection [Optional]
            * Classification Selection [Optional]
        - Table Selection
        - Variable-Value Selection
        -- Serie Selection
            * Graph Selection.
            * Axis Selection.
    """
    element = html.Div(
        children=[
            op_comp,
            html.Div(
                children=[
                    tab_comp,
                    varvalbox_comp
                ],
                className='ColSplitterBase ColSplitterBig',
                **{'id': UIM.id_generator(ui_type='Arranger',
                                          ui_name='TablaVVP',
                                          row_lv1=row_lv1)}
            )
        ],
        **{'id': UIM.id_generator(ui_type='Arranger',
                                  ui_name='InputsGroupRow',
                                  row_lv1=row_lv1)}
    )
    return element


def InputSelectionBox(initial_IGR):
    component = html.Div(
        children=[
            html.Div(
                [initial_IGR],
                className='RowSplitterBase RowSplitterBig',
                **{'id': UIM.id_generator(ui_type='Arranger',
                                          ui_name='InputSelection')}
            ),
            NewRowButtonComp('InputSelection', None)
        ],
        **{'id': UIM.id_generator(ui_type='Arranger',
                                  ui_name='InputSelection',
                                  ui_subtype='Box')}
    )
    return component


def make_IGR(row_lv1):
    OpC = OperationSelectBox(row_lv1)
    TbC = TableSelectBox(row_lv1, list())
    VVP = make_vvp(row_lv1, 1)
    return InputsGroupRow(row_lv1, OpC, TbC, VVP)



