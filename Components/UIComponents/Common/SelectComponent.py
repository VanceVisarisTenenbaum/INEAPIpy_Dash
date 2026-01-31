# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 18:46:04 2025

@author: mano
"""

from dash import dcc
from Components.UIComponents.Managers.UIManager import UIManager
from Components.UIComponents.Common.Styles import SELECT_INPUT_STYLE
from Components.UIComponents.Common.LabelInput import LabelInput
from Components.SharedFunctions import extract_labels_values


UIM = UIManager()
def SelectComponent(list_of_ine_obj,
                    name,
                    fila_lv1, fila_lv2=None,
                    multi=False):
    """Returns a select for variables or values."""
    list_of_labels_values = extract_labels_values(list_of_ine_obj)
    if multi:
        placeholder = 'Selecciona una o varias ' + name
    else:
        placeholder = 'Selecciona una '  + name
    # Adds initial empty value
    InputComponent = dcc.Dropdown(
        options=list_of_labels_values,
        value=None,  # Default value is empty
        **{'id': UIM.id_generator(ui_type='Input',
                                  ui_name=name,
                                  ui_subtype='Dropdown',
                                  row_lv1=fila_lv1,
                                  row_lv2=fila_lv2)},
        style=SELECT_INPUT_STYLE,
        multi=multi,
        placeholder=placeholder
    )

    component = LabelInput(name, InputComponent, 'top')
    return component