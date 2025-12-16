# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 13:18:13 2025

@author: mano
"""

from dash import html


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








