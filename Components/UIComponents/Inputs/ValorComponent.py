# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 13:35:06 2025

@author: mano
"""


from Components.UIComponents.Common.SelectComponent import SelectComponent



def ValorComponent(row_lv1, row_lv2, list_of_ine_val):
    component = SelectComponent(list_of_ine_val, 'Valor', row_lv1, row_lv2)
    return component
