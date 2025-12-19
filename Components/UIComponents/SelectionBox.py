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
from Components.UIComponents.Common.id_generator import id_generator_mapper

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
                **{'id': id_generator_mapper('TablaVVP', 'Box', row_lv1)}
            )
        ],
        **{'id': id_generator_mapper('IG', None, row_lv1)}
    )
    return element


def InputSelectionBox(initial_IGR):
    component = html.Div(
        children=[initial_IGR],
        className='RowSplitterBase RowSplitterBig',
        **{'id': 'ISB'}
    )
    return component

