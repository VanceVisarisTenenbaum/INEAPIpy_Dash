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

from dash import dcc

from Components.UIComponents.Common.LabelInput import LabelInput
from Components.UIComponents.Common.Styles import SELECT_INPUT_STYLE
from Components.UIComponents.Common.id_generator import id_generator_mapper
from Components.SharedFunctions import extract_labels_values
from Components.Storage.ServerMemory import ServerMemoryManager


def OperationSelectBox(row_number):

    SSM = ServerMemoryManager()


    options = [
        extract_labels_values(op)
        for op in SSM.get_metadata('Operaciones')
    ]
    InputComponent = dcc.Dropdown(
        options=options,
        value=None,  # Default value is empty
        **{'id': id_generator_mapper('O', None, row_number)},
        style=SELECT_INPUT_STYLE
    )

    component = LabelInput('Operaciones', InputComponent)
    return component

"""
Asociado con la Operación, cuando un usuario selecciona un operación, es
necesario generar los inputs que permiten seleccionar una tabla y los
inputs que permiten seleccionar los pares variable-valor.
"""



