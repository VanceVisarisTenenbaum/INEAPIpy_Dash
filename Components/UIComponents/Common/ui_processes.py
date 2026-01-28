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
        State('StateStorage', 'data')
    ]
    return inputs

def DUMMY_INPUT(name='', state=False):
    if state:
        return State('DummyStorage' + str(name), 'data')
    return Input('DummyStorage' + str(name), 'data')

def STORAGE_OUTPUTS(duplicates_list=[True, True]):

    order_list = ['RequestsStorage', 'StateStorage']
    outputs = list()
    for i, storage in enumerate(order_list):
        outputs.append(Output(storage, 'data',
                              allow_duplicate=duplicates_list[i]))

    return outputs

def DUMMY_OUTPUT(name='', allow_duplicate=False):
    return Output('DummyStorage'+str(name), 'data',
                  allow_duplicate=allow_duplicate)



def _str_to_match(matching_type):
    if matching_type == 'ALL':
        return ALL
    elif matching_type == 'MATCH':
        return MATCH
    elif matching_type == 'ALLSMALER':
        return ALLSMALLER
    else:
        return matching_type

def _type_to_io(input_type, id_, prop):
    if input_type == 'Output':
        return Output(id_, prop)
    elif input_type == 'Input':
        return Input(id_, prop)
    elif input_type == 'State':
        return State(id_, prop)
    return None


def io_generator(input_type: str, name: str, tipo: str,
                 row_lv1 = None, row_lv2 = None, prop=None):
    """
    Generates a State, Output or Input with the proper ID.

    Parameters
    ----------
    input_type : Literal[Input | Output | State]
        String indicanting the Input or Output type.
    name : str
        Name for the type of the ID generator.
    tipo : str
        Tipo for the ID generator
    row_lv1 : int | str, optional
        str indicating a matching pattern or int specifying.
        The default is None.
    row_lv2 : int | str, optional
        str indicating a matching pattern or int specifying.
        The default is None.
    prop : TYPE, optional
        Property to grab from the document object. The default is None.

    Returns
    -------
    dash.Input | dash.Output | dash.State
        the dash Input Output object.

    """

    row_lv1 = _str_to_match(row_lv1)
    row_lv2 = _str_to_match(row_lv2)
    # si alguno es None, la siguiente función no los añade.
    id_ = id_generator_mapper(name, tipo, row_lv1, row_lv2)

    return _type_to_io(input_type, id_, prop)