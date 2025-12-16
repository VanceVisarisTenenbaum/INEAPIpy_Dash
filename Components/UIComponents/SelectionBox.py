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
from Components.UIComponents.OperationBox import OperationSelectBox
from Components.UIComponents.TableComponent import TableSelectBox
from Components.UIComponents.VarValPairsBox import VarValPairBoxComponent
from Components.UIComponents.Common.id_generator import id_generator_mapper
from Components.UIComponents.Common.Styles import (COLUMN_SEPARATED_DIVS,
                                                   ROW_SEPARATED_DIVS)


def InputsGroupRow(row_number):
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
            OperationSelectBox(row_number),
            html.Div(
                children=[
                    TableSelectBox(row_number),
                    VarValPairBoxComponent(row_number)
                ],
                style=COLUMN_SEPARATED_DIVS
            )
        ],
        **{'id': id_generator_mapper('IG', None, row_number)}
    )
    return element


def InputSelectionBox():
    component = html.Div(
        children=[InputsGroupRow(1)],
        style=ROW_SEPARATED_DIVS,
        **{'id': 'ISG'}
    )
    return component

