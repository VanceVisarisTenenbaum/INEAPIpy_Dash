# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 13:26:48 2025

@author: mano
"""

from dash import Input, Output, State, ALL, MATCH, ALLSMALLER
from Components.UIComponents.Common.id_generator import id_generator_mapper

def add_new_son(old_sons_list, new_son):
    for son in old_sons_list:
        if son['props']['id'] == new_son.id:
            # Si encuentra un hijo con el mismo id no se actualiza.
            return old_sons_list
    old_sons_list.append(new_son)
    return old_sons_list

def remove_sons(sons_list, starting_index):
    return sons_list[:starting_index]


def STORAGE_INPUTS():
    inputs = [
        State('RequestsStorage', 'data'),
        State('StateStorage', 'data'),
        Input('DummyStorage', 'data'),
    ]
    return inputs


def STORAGE_OUTPUTS(duplicates_list=[True, True, True]):

    order_list = ['RequestsStorage', 'StateStorage', 'DummyStorage']
    outputs = list()
    for i, storage in enumerate(order_list):
        outputs.append(Output(storage, 'data',
                              allow_duplicate=duplicates_list[i]))

    return outputs



def _tr_to_match(matching_type):
    return None

def io_generator(input_type: str, name: str, tipo: str,
                 row_lv1: int = None, matching_type = None):


    if row_lv1 is not None:
        id_ = id_generator_mapper(name, tipo, row_lv1)
    else:
        id_ = id_generator_mapper(name, tipo)

    if row_lv1 is not None:
        if matching_type is not None:
            id_['row_lv2'] =

    return result