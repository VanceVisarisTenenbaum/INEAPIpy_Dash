# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 18:46:04 2025

@author: mano
"""

from dash import dcc
from Components.UIComponents.Common.id_generator import (id_generator_mapper,
                                                         name_mapper)
from Components.UIComponents.Common.Styles import SELECT_INPUT_STYLE
from Components.UIComponents.Common.LabelInput import LabelInput
from Components.SharedFunctions import extract_labels_values

def SelectComponent(list_of_ine_obj,
                    name,
                    fila_lv1, fila_lv2=None,
                    multi=False):
    """Returns a select for variables or values."""
    list_of_labels_values = extract_labels_values(list_of_ine_obj)
    if multi:
        placeholder = 'Selecciona una o varias ' + id_generator_mapper(name)
    else:
        placeholder = 'Selecciona una '  + id_generator_mapper(name)
    # Adds initial empty value
    InputComponent = dcc.Dropdown(
        options=list_of_labels_values,
        value=None,  # Default value is empty
        **{'id': id_generator_mapper(name, None, fila_lv1, fila_lv2)},
        style=SELECT_INPUT_STYLE,
        multi=multi,
        placeholder=placeholder
    )

    component = LabelInput(name_mapper(name), InputComponent, 'top')
    return component