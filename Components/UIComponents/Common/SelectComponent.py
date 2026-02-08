# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 18:46:04 2025

@author: mano
"""

from dash import dcc, html
from Components.UIComponents.Managers.UIManager import UIManager
from Components.UIComponents.Common.LabelInput import LabelInput
from Components.SharedFunctions import extract_labels_values


UIM = UIManager()
def SelectComponent(list_of_ine_obj,
                    name,
                    fila_lv1, fila_lv2=None,
                    multi=False):
    """Returns a select for variables or values."""
    list_of_labels_values = extract_labels_values(list_of_ine_obj)

    """
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
        className='Input Dropdown',
        multi=multi,
        placeholder=placeholder
    )

    #component = LabelInput(name, InputComponent, 'top')
    """

    summary = html.Summary(
        children=[
            html.H3(name),
            html.Span('', className='svg chevron-down')
        ],
        className='collapse-header'
    )

    selection = dcc.RadioItems(
        options=list_of_labels_values,
        className='radio-custom',
        value=None,
        **{'id': UIM.id_generator(ui_type='Input',
                                  ui_name=name,
                                  ui_subtype='Dropdown',
                                  row_lv1=fila_lv1,
                                  row_lv2=fila_lv2)},
    )
    component = html.Details(
        children=[
            summary,
            html.Div(
                selection,
                className='collapse-content'
            )
        ],
        className='custom-collapse'
    )
    return component