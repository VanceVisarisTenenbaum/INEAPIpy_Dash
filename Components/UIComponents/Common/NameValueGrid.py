# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 14:40:44 2025

@author: mano
"""


from dash import html


def dict_value_process(val):
    if isinstance(val, list) or isinstance(val, tuple):
        new_val = ''
        for i,v in enumerate(val):
            if i%3 == 0:
                sep = '\n'
            else:
                sep = '; '
            new_val = str(v) + sep
    elif isinstance(val, dict):
        raise ValueError("val can't be a dict.")
    else:
        new_val = str(new_val)
    return new_val


def NameValue(name_value_dict):
    childrens = list()
    for k,v in name_value_dict.items():
        comp = html.Div(
            children=[
                html.Span(k,
                        className='NameValName'),
                html.Span(dict_value_process(v),
                          className='NameValVal')
            ],
            className='NameValue'
        )
        childrens.append(comp)

    component = html.Div(
        children=childrens,
        className='NameValueGrid'
    )
    return component


def NameValueDisplayComponent(name_value_dict, comp_id, title=None):

    if title is None:
        component = html.Div(
            children = [
                NameValue(name_value_dict)
            ],
            **{'id': comp_id}
        )
    else:
        component = html.Div(
            children = [
                html.H2(title),
                NameValue(name_value_dict)
            ],
            **{'id': comp_id}
        )
    return component