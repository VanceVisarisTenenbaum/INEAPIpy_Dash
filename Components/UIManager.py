# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 14:27:27 2025

@author: mano
"""

from dash import html, callback, Input, Output, State

from Components.Storage.SingletonCustom import SingletonMeta
from Components.Storage.RequestsStorage import RequestsStorageManager
from Components.Storage.StateStorage import StateStorageManager
from Components.Storage.ServerMemory import ServerMemoryManager
from Components.Storage.DummyStorage import DummyStorageManager

from Components.UIComponents.ValorComponent import ValorComponent
from Components.UIComponents.VariableComponent import VariableComponent
from Components.UIComponents.VarValPairsBox import VarValPair
from Components.UIComponents.TableComponent import TableSelectBox
from Components.UIComponents.SelectionBox import (InputsGroupRow,
                                                  InputSelectionBox)

from Components.UIComponents.Common.id_generator import id_generator_mapper


"""
This module contains the class that allows to manage the events that will
happen when the user interacts with the interface.
"""

"""
UIManager handles the UI trasformations.

This means it takes care of all the event listener processes.
"""
class UIManager(metaclass=SingletonMeta):
    """Provides methods to manage the UI different states."""
    def __init__(self):
        self.__RSM = RequestsStorageManager()
        self.__SSM = StateStorageManager()
        self.__SMM = ServerMemoryManager()
        self.__DSM = DummyStorageManager()
        return None

    def __add_new_son(self, old_sons_list, new_son):
        for son in old_sons_list:
            if son['props']['id'] == new_son.id:
                # Si encuentra un hijo con el mismo id no se actualiza.
                return old_sons_list
        old_sons_list.append(new_son)
        return old_sons_list

    def __remove_sons(self, sons_list, starting_index):
        return sons_list[:starting_index]

    def __make_var_val_comp(self, op_id, row_lv1, row_lv2, session_storage):
        variables, session_storage = self.__RSM.get_obj('Variable',
                                                        op_id,
                                                        session_storage)
        VrC = VariableComponent(row_lv1, row_lv2, variables)
        VlC = ValorComponent(row_lv1, row_lv2, list())
        return VarValPair(VrC, VlC, row_lv1, row_lv2)

    def __make_tab_comp(self, op_id, row_lv1, session_storage):
        tablas, session_storage = self.__RSM.get_obj('Tabla',
                                                     op_id,
                                                     session_storage)
        return TableSelectBox(row_lv1, tablas)

    # ------------------------------------------------------------------------
    # PROCESO PARA AÑADIR EVENT LISTENERS
    # VALOR
    def select_valor_listener(self, row_lv1, row_lv2):
        """
        Adds the event listener to the Valor Select.

        Cuando el usuario seleccionar un valor ocurre lo siguiente:
            1- Se guarda el valor elegido en el almacenamiento de estado.

        Los inputs necesarios son:
            1- La operación elegida previamente.
            2- La variable elegida previamente.
            3- El valor elegido.
            4- El almacenamiento de estado.

        La salida debe ser:
            1- El almacenamiento de estado.
        """
        @callback(
            Output('StateStorage', 'data'),
            State(
                id_generator_mapper('O', None, row_lv1),
                'value'
            ),
            State(
                id_generator_mapper('Vr', None, row_lv1, row_lv2),
                'value'
            ),
            Input(
                id_generator_mapper('Vl', None, row_lv1, row_lv2),
                'value'
            ),
            State('ResquestsStorage', 'data'),
            State('StateStorage', 'data')
        )
        def process(op_id, var_id, val_id, state_storage):
            if not isinstance(val_id, int):
                return state_storage
            state_storage = self.__SSM.update_selected_value(op_id,
                                                             var_id,
                                                             None, val_id,
                                                             state_storage)
            return state_storage
        return None

    # ------------------------------------------------------------------------
    # VARIABLE
    def select_variable_listener(self, row_lv1, row_lv2):
        """
        Adds the event listener to the Variable Select.

        Cuando el usuario selecciona una variable ocurre lo siguiente:
            1- Se cargan los valores asociados a dicha variable.
            2- Se actualizan los valores del select de valores asociado.
            3- Se actualiza el estado de la app.
            4- Se añade una nueva fila para la selección de variables.

        Para conseguir esto los inputs son:
            1- La Operación elegida previamente.
            2- La variable elegida.
            3- el almacenamiento de peticiones.
            4- el almacenamiento de estado.
            5- los hijos del contenedor padre.

        Las salidas son:
            1- Las opciones del select de valor asociado.
            2- El almacenamiento de peticiones.
            3- El almacenamiento de estado.
            4- Las hijos del contenedor padre.
        """
        dummy_name = self.__DSM.namer('Var', row_lv1, row_lv2)
        @callback(
            Output(
                id_generator_mapper('Vl', None, row_lv1, row_lv2),
                'options'
            ),
            Output('RequestsStorage', 'data'),
            Output('StateStorage', 'data'),
            Output('DummyStorage', 'data'),
            State(
                id_generator_mapper('O', None, row_lv1),
                'value'
            ),
            Input(
                id_generator_mapper('Vr', None, row_lv1, row_lv2),
                'value'
            ),
            State('ResquestsStorage', 'data'),
            State('StateStorage', 'data'),
            State('DummyStorage', 'data')
        )
        def process(op_id, var_id,
                    session_storage, state_storage,
                    dummy_storage):

            if not isinstance(var_id, int):
                return list(), session_storage, state_storage, parent_childrens

            # 1- Actualizamos el estado
            state_storage = self.__SSM.update_selected_variable(
                op_id,
                None, var_id,
                state_storage
            )
            # 2- Obtenemos los valores asociados a dicha variable
            valores, session_storage = self.__RSM.get_obj('Valor',
                                                          var_id,
                                                          session_storage)



            # 4- Actualizamos el dummy storage para indicar que este fue el
            # último proceso.
            dummy_storage = self.__DSM.add_update(dummy_name, dummy_storage)
            return (valores,
                    session_storage,
                    state_storage,
                    dummy_storage)

        # Añadimos el proceso para añadir una nueva fila.
        @callback(
            Output(
                id_generator_mapper('VariableValor', None, row_lv1, row_lv2),
                'children'
            ),
            State(
                id_generator_mapper('O', None, row_lv1),
                'value'
            ),
            Input(
                id_generator_mapper('Vr', None, row_lv1, row_lv2),
                'value'
            ),
            State(
                id_generator_mapper('VariableValor', None, row_lv1, row_lv2),
                'children'
            ),
            State('ResquestsStorage', 'data'),
            Input('DummyStorage', 'data')
        )
        def new_row(op_id, var_id,
                    parent_childrens,
                    session_storage, dummy_storage):
            if self.__DSM.get_last_update(dummy_storage) != dummy_name:
                # En caso que el ultimo proceso no fuese el del mismo
                # event listener no se ejecuta.
                return parent_childrens
            # 3- Generamos una nueva fila
            VVP = self.__make_var_val_comp(op_id,
                                           row_lv1, row_lv2,
                                           session_storage)
            # Le añadimos los event listener a la nueva fila.
            self.select_variable_listener(row_lv1, row_lv2 + 1)
            self.select_valor_listener(row_lv1, row_lv2 + 1)

            # Borramos todos los elementos elegidos en adelante y
            # añadimos la nueva fila.
            new_childrens = self.__remove_sons(parent_childrens, row_lv2)
            new_childrens = self.__add_new_son(new_childrens, VVP)

            return new_childrens
        return None

    # ------------------------------------------------------------------------
    # OPERACION
    def select_operation_listener(self, row_lv1):
        """
        Adds the event listener to the OP Select

        El select de Operación tiene que tener un event listener para saber
        cuando el usuario ha seleccionado una opearción.

        Cuando esto ocurre, se ejecutan los siguientes pasos:
            1- Se guarda la seleccion en el estado.
            2- Se cargan las tablas asociadas.
            3- Se cargan las variables asociadas.
            4- Se genera el componente Select de las tablas.
            5- Se genera el componente con los pares variable-valor.
            6- Se genera el div que contiene las tablas y los var-val.
            7- Se genera una nueva fila para la selección de operación.

        Para cumplir esto, el input es:
            1- la operación elegida.
            2- el almacenamiento de peticiones.
            3- el almacenamiento de estado.
            4- los hijos del contenedor padre.

        Las salidas deben ser:
            1- Los hijos de la caja TablaVVPBox_row_lv1
            2- El almacenamiento de peticiones
            3- El almacenamiento de estado.
            4- Los hijos del contenedor padre con el nuevo hijo añadido.
        """
        dummy_name = self.__DSM.namer('O', row_lv1)
        @callback(
            Output(
                id_generator_mapper('TablaVVP', 'Box', row_lv1),
                'children'
            ),
            Output('RequestsStorage', 'data'),
            Output('StateStorage', 'data'),
            Output('DummyStorage', 'data'),
            Input(
                id_generator_mapper('O', None, row_lv1),
                'value'
            ),
            State('RequestsStorage', 'data'),
            State('StateStorage', 'data'),
            State('DummyStorage', 'data')
        )
        def process(op_id,
                    session_storage, state_storage,
                    dummy_storage):

            if not isinstance(op_id, int):
                return list(), session_storage, state_storage
            # 1- Actualizamos el estado.
            state_storage = self.__SSM.update_selected_operation(None, op_id,
                                                                 state_storage)

            # 2- Creamos el select de tabla y el par Var-Val
            TC = self.__make_tab_comp(op_id, row_lv1, session_storage)
            VVP = self.__make_var_val_comp(op_id, row_lv1, 1, session_storage)
            # Le añadimos los event listener
            self.select_variable_listener(row_lv1, 1)
            self.select_valor_listener(row_lv1, 1)
            # 1 por que es el inicial.
            TabVVPChildrens = [TC, VVP] # Por que se juntan en un div.

            # 4- Actualizamos el dummy storage para indicar que este fue el
            # último proceso.
            dummy_storage = self.__DSM.add_update(dummy_name, dummy_storage)

            return (TabVVPChildrens,
                    session_storage, state_storage,
                    dummy_storage)

        """
        Como no podemos añadir el select de tablas y Var-Val al mismo tiempo
        que añadimos una nueva fila, separamos el processo de añadir nueva
        fila en un segundo callback.
        """
        @callback(
            Output('ISB', 'children'),
            Input(
                id_generator_mapper('O', None, row_lv1),
                'value'
            ),
            State('ISB', 'children'),
            Input('DummyStorage', 'data'), # Esto hace que se ejecute cuando
            # se actualice el dummy.
        )
        def new_row_process(op_id, parent_childrens, dummy_storage):
            if self.__DSM.get_last_update(dummy_storage) != dummy_name:
                # En caso que el ultimo proceso no fuese el del mismo
                # event listener no se ejecuta.
                return parent_childrens

            # 3- Creamos la siguiente fila.
            next_box = InputsGroupRow(row_lv1 + 1)
            # Añadimos los event listener a la nueva fila.
            self.select_operation_listener(row_lv1 + 1)
            # Añadimos la fila a la lista de hijos
            parent_childrens = self.__add_new_son(parent_childrens, next_box)

            return parent_childrens
        return None

    def initial_setup(self):

        component = html.Div(
            children=[
                self.__RSM.get_initial_requests_storage(),
                self.__SSM.get_initial_state_storage(),
                InputSelectionBox()
            ],
            **{'id': 'main'}
        )
        self.select_operation_listener(1)
        return component



























