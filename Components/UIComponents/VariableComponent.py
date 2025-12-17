# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 13:34:22 2025

@author: mano
"""


from Components.UIComponents.Common.SelectComponent import SelectComponent

def VariableComponent(row_lv1, row_lv2, list_of_ine_vars):
    component = SelectComponent(list_of_ine_vars, 'Vr', row_lv1, row_lv2)
    return component