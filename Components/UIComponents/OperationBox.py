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


def OperationSelectBox(row_number):
    SSM = ServerMemoryManager()
    return SelectComponent(SSM.get_metadata('Operaciones'), 'O', row_number)

"""
Asociado con la Operación, cuando un usuario selecciona un operación, es
necesario generar los inputs que permiten seleccionar una tabla y los
inputs que permiten seleccionar los pares variable-valor.
"""



