# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 13:18:13 2025

@author: mano
"""

from dash import html

"""
This file contains some variables that should be constants in the app, plus
some additional functions.
"""

# Cargamos todas las variables que se mantendrán constantes mientras se este
# usando el servidor.

"""
Definimos algunos estilos reutilizables.
"""
COMMON_PADDING = '6px'

SELECT_INPUT_STYLE = {
    'width': '500px',
    'height': '100px',
    'padding': COMMON_PADDING
}


"""
Definimos una serie de componentes sencillos que se utilizarán en el resto
de componentes.
"""

def LabelInput(label, inputComponent, style='top'):

    if style == 'top':
        component = html.Div(
            children=[html.Span(label), inputComponent],
            style={'display': 'flex',
                   'flex-direction': 'column',
                   'alignItems': 'left',
                   'marginBottom': '20px',
                   'padding': COMMON_PADDING,
                   'font-size': '40px'}
        )
    elif style == 'side':
        component = html.Div(
            children=[html.Span(label), inputComponent],
            style={'display': 'block', 'marginTop': '20px'}
        )
    else:
        raise ValueError('style can only be "top" or "side"')
    return component

"""
Definimos algunas funciones útiles.
"""

def _extract_label_value(INE_object, only_id: bool = False):
    if isinstance(INE_object, dict):
        if only_id:
            return INE_object['Id']
        return {'label': INE_object['Nombre'], 'value': INE_object['Id']}
    else:
        raise TypeError('INE_object must be dict.')


def extract_labels_values(list_of_INE_objects, only_id: bool = False):
    if isinstance(list_of_INE_objects, list):
        return [_extract_label_value(x, only_id) for x in list_of_INE_objects]
    elif isinstance(list_of_INE_objects, dict):
        return _extract_label_value(list_of_INE_objects, only_id)
    else:
        raise TypeError('list of INE objects must be a list or dict.')


def check_if_loaded(INE_id: int, INE_obj_var: str, session_storage):
    """
    Checks if the INE_id has been loaded already.

    INE_id: int
        The ID from INE object to check if it is already loaded.
    INE_obj_var: Literal['Operacion' | 'Variable']
        The type to check. If an Operacion or Variable is already loaded in
        session storage
    session_storage:
        The session storage.
    """
    if not isinstance(INE_id, int):
        raise TypeError('INE_id is not an int.')
    if INE_obj_var == 'Operacion':
        return INE_id in session_storage['OperacionesSolicitadas']
    elif INE_obj_var == 'Variable':
        return INE_id in session_storage['VariablesSolicitadas']
    else:
        raise ValueError('INE_obj_var is not a valid value.')


def state_storage_base():
    initial_dict = {
        'Operacion': None,
        'Tabla': None,
        'VariableValor': [
            {
                'Variable': None,
                'Valor': None
            }
        ],
        'Serie': [
            {
                'Serie': None,
                'Grafica': {
                    'NGrafica': None,
                    'Eje': None,
                    'Estilo': None
                }
            }
        ]
    }
    return initial_dict

def select_op_row_from_state(op_id, state_storage):
    for row in state_storage:
        if row['Operacion'] == op_id:
            return row
    return None






