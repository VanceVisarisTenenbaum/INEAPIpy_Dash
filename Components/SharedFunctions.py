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
                   'marginBottom': '20px'}
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
Definimos algunos estilos reutilizables.
"""

SELECT_INPUT_STYLE = {
    'width': '500px',
    'height': '100px',
    'padding': '6px'
}


"""
Definimos algunas funciones útiles.
"""

def _extract_label_value(INE_object):
    if isinstance(INE_object, dict):
        return {'label': INE_object['Nombre'], 'value': INE_object['Id']}
    else:
        raise TypeError('INE_object must be dict.')


def extract_labels_values(list_of_INE_objects):
    if isinstance(list_of_INE_objects, list):
        return [_extract_label_value(x) for x in list_of_INE_objects]
    elif isinstance(list_of_INE_objects, dict):
        return _extract_label_value(list_of_INE_objects)
    else:
        raise TypeError('list of INE objects must be a list or dict.')

