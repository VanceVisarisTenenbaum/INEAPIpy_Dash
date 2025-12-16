# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 20:30:38 2025

@author: mano
"""

from Components.UIComponents.Common.SelectComponent import SelectComponent


def TableSelectBox(row_number):
    return SelectComponent(list(), 'T', row_number)