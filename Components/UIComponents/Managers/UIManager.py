# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 22:34:29 2026

@author: mano
"""

from dash import Input, Output, State, ALL, MATCH, ALLSMALLER

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

-------------------------------------------------------------------------------

Given this UI, we can distinguish the next components.

- Inputs, those that allow the user to select wether the Operation, Serie, etc.
- Arrangers, those that manage the layout of its inner components, such as, InputsBox
- Display, those that display information.
"""

class UIManager(metaclass=SingletonMeta):
    """Class that takes care of getting IDs, names, or more about UI"""
    def __init__(self):
        self.__available_ui_types = [
            'Arranger', 'Input', 'Storage', 'Label', 'Container'
        ]
        self.__available_subtypes = [
            None,
            'Dropdown',
            'Button',
            'Client',
            'Server',
            'Box',
            'Checkbox',
            'Row',
            'Series',
            'Selected_Series'
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
        self.__io_types = ['Input', 'Output', 'State']
        self.__wildcards_map = {
            'ALL': ALL,
            'MATCH': MATCH,
            'ALLSMALLER': ALLSMALLER
        }
        return None

    def __check_valid_ui_type(self, ui_type):
        if ui_type not in self.__available_ui_types:
            raise ValueError(str(ui_type) + ': Is not valid ui_type.')
        return True

    def __check_valid_subtype(self, input_type):
        if input_type not in self.__available_subtypes:
            raise ValueError(str(input_type) + ': Is not valid input_subtype.')
        return True

    def __checks(self, ui_type, ui_subtype):
        self.__check_valid_ui_type(ui_type)
        self.__check_valid_subtype(ui_subtype)
        return True

    def __val_to_wildcard(self, value):
        """Returns the wildcard if possible, else return the input value."""
        if value is None:
            value=''
        wildcard = self.__wildcards_map.get(str(value).upper(), value)
        return wildcard

    def id_generator(self, ui_type=None, ui_name=None, ui_subtype=None,
                     row_lv1=None, row_lv2=None):
        self.__checks(ui_type, ui_subtype)

        ui_id = {
            'Tipo': self.__val_to_wildcard(ui_type),
            'Nombre': self.__val_to_wildcard(ui_name),
            'Subtipo': self.__val_to_wildcard(ui_subtype),
            'Fila Nivel 1': self.__val_to_wildcard(row_lv1),
            'Fila Nivel 2': self.__val_to_wildcard(row_lv2)
        }
        return ui_id

    def __check_io_type(self, io_type):
        if io_type not in self.__io_types:
            raise ValueError(str(io_type) + ': Is not a valid io_type.')
        return None


    def io_generator(self, io_type=None, io_prop=None,
                     allow_optional=False,
                     allow_duplicate=False,
                     **id_gen_kwargs):

        self.__check_io_type(io_type)
        io_map = {
            'INPUT': Input(
                self.id_generator(**id_gen_kwargs),
                io_prop,
                allow_optional
            ),
            'STATE': State(
                self.id_generator(**id_gen_kwargs),
                io_prop,
                allow_optional
            ),
            'OUTPUT': Output(
                self.id_generator(**id_gen_kwargs),
                io_prop,
                allow_duplicate
            )
        }

        return io_map.get(str(io_type).upper(), None)

    # End of class







































