# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 22:34:29 2026

@author: mano
"""

from Components.Storage.SingletonCustom import SingletonMeta

"""
The UI Components follow a defined convention, in order to maintain the
convention in the app we define a function that returns the expected ID
for any component.

The UI is composed as follows:
-
Input Selections Box
    Inputs Group Row 1
    Inputs Group Row 2
    ...
        Operation Selection Box
            -- Label Operacion
            -- Select Operacion
            -- Display Info Operacion
                -- H2 Operacion
                -- Grid with Info
        Table Selection Box
            -- Label Tabla
            -- Select Tabla
            -- Display Info Tabla
                --
                --
        Variable Value Selection Box
            Variable Valor Row 1
            Variable Valor Row 2
            ...
                Variable Selection Box
                    -- Label Variable
                    -- Select Variable
                Valor Selection Box
                    -- Label Valor
                    -- Select Valor
        Load Series Button
        Serie Selection Box
            -- Label Series
            -- MultiSelect Series
            -- Display Info Series
                --
                --
            -- Select Gráfica
            -- Select Eje
            -- Select Estilo
Graph Display Box
    Graph Display 1
    Graph Display 2
    ...
        -- Label Gráfica
        -- Display Gráfica
"""

class UIManager(metaclass=SingletonMeta):
    """Class that takes care of getting IDs, names, or more about UI"""
    def __init__(self):
        self.__available_ui_types = [
            'Arranger', 'Input'
        ]
        self.__available_input_types = [
            'Select',
            'Dropdown',
            'Button'
        ]
        self.__input_names = [
            'Operacion',
            'Variable',
            'Valor',
            'Tabla',
            'Serie',
            'Graph',
            'Graph Axis',
            'Graph Style'
        ]
        return None

    def __check_valid_ui_type(self, ui_type):
        if ui_type not in self.__available_ui_types:
            raise ValueError(str(ui_type) + ': Is not valid ui_type.')
        return True

    def __check_valid_input_type(self, input_type):
        if input_type not in self.__available_input_types:
            raise ValueError(str(input_type) + ': Is not valid input_type.')
        return True

    def __checks(self, ui_type, input_type):
        self.__check_valid_ui_type(ui_type)
        self.__check_valid_input_type(input_type)
        return True

    def id_generator(self, ui_type, ui_name, input_type=None,
                     row_lv1=None, row_lv2=None):
        self.__checks(ui_type, input_type)
        ui_id = {
            'Tipo': ui_type,
            'Nombre': ui_name,
            'Input Type': input_type,
            'Fila Nivel 1': row_lv1,
            'Fila Nivel 2': row_lv2
        }
        return ui_id
    # End of class







































