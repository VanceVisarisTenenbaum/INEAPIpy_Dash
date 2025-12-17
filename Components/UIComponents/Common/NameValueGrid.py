# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 14:40:44 2025

@author: mano
"""


from dash import html
from Components.UIComponents.Common.Styles import (SPAN_INFO_NAME_STYLE,
                                                   SPAN_INFO_VALUE_STYLE,
                                                   NAME_VALUE_DISPLAY_STYLE,
                                                   NAME_VALUE_DISPLAY_GRID_STYLE)


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
                html.span(k,
                        style=SPAN_INFO_NAME_STYLE),
                html.span(dict_value_process(v),
                          style=SPAN_INFO_VALUE_STYLE)
            ],
            style=NAME_VALUE_DISPLAY_STYLE
        )
        childrens.append(comp)

    component = html.Div(
        children=childrens,
        style=NAME_VALUE_DISPLAY_GRID_STYLE
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
                html.h2(title),
                NameValue(name_value_dict)
            ],
            **{'id': comp_id}
        )
    return component