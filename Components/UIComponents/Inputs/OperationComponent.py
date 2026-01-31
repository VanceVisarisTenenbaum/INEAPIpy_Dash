# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 22:25:24 2025

@author: mano
"""

"""
This file contains the function that creates a select for one Operation,
with two additional optional selects, Periodicity and Classification.
"""


from Components.Storage.ServerMemory import ServerMemoryManager


from Components.UIComponents.Common.SelectComponent import SelectComponent



def OperationSelectBox(row_lv1):
    SSM = ServerMemoryManager()
    return SelectComponent(SSM.get_metadata('Operaciones'), 'Operacion', row_lv1)





