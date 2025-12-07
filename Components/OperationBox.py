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

from dash import html, dcc
from .SharedFunctions import SERVER_MEMORY, LabelInput, SELECT_INPUT_STYLE


def OperationSelectBox(row_number):

    options = [
        {'label': op['Nombre'], 'value': op['Id']}
        for op in SERVER_MEMORY['Operaciones']
    ]
    inputComponent = dcc.Dropdown(
        options=options,
        value=None,  # Default value is empty
        **{'id': 'OpSelect_' + str(row_number)},
        style=SELECT_INPUT_STYLE
    )

    component = LabelInput('Operaciones', inputComponent)
    return component
