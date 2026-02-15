# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 11:42:39 2025

@author: mano
"""

from dash import dcc
from Components.Storage.SingletonCustom import SingletonMeta
from Components.Storage.ServerMemory import ServerMemoryManager
from Components.UIComponents.Managers.UIManager import UIManager

"""
Session Storage is a client side store meant to store all the requests made by
the user.

It is preferable to be this way since storing all the requests in server will
end in the server storing all the INE database.

This way the server acts only as a middle man that manages all the requests to
the INE.

The downside is that it will make the requests for the end user a bit slower
multiplying the effect for each user using the app.

The upside, it keeps the INE usage under stricter control.
"""

"""
The server already stores some information in its memory. Check ServerMemory.

The session storage on the other hand have the next shape:
    {
         'Variables': {op_id: [INEVariablesObjects]},
         'Valores': {var_id: [INEValorObjects]},
         'Tablas': {tab_id: [INETablaObjects]},
         'Periodo': {},
    }
"""

UIM = UIManager()
class RequestsStorageManager(metaclass=SingletonMeta):
    """Server component that manages the retrieval of data from the storage"""

    """
    All the methods in this class are meant to work with the client session
    storage, this means that all methods will take the session storage as
    input and will return the same session storage if it was necessary to
    modify it, in order for the client to be kept update at all time.
    """
    def __init__(self):
        self.SSM = ServerMemoryManager()

        self.initial_storage = {
            'Variable': dict(),
            'Valor': dict(),
            'Tabla': dict(),
            'Periodo': dict(),
            'Serie': dict(),
            'Data': dict(),
            'Operaciones': self.SSM.get_metadata('Operaciones'),
            'Publicaciones': self.SSM.get_metadata('Publicaciones'),
            'Unidades': self.SSM.get_metadata('Unidades'),
            'Escalas': self.SSM.get_metadata('Escalas'),
            'Periodicidades': self.SSM.get_metadata('Periodicidades')
        }

        requests_storage = dcc.Store(**{'id': UIM.id_generator(
                                            ui_type='Storage',
                                            ui_name='Requests',
                                        ),
                                       'storage_type': 'session'},
                                    data=self.initial_storage)
        self.__initial_requests_storage = requests_storage
        return None

    def get_initial_requests_storage(self):
        return self.__initial_requests_storage

    def __check_type(self, val: int, name: str=''):
        """Checks if the input was an int. Name is for debugging."""
        if not isinstance(val, int):
            raise TypeError('Input is not an int. Where: ' + str(name))
        return None

    def __check_dict_type(self, filtering_dict: dict, name: str=''):
        """Checks if the input was an dict. Name is for debugging."""
        if not isinstance(filtering_dict, dict):
            raise TypeError('Input is not an dict. Where: ' + str(name))
        return None

    def __check_metadata_filter(self, metadata: dict, name: str=''):
        self.__check_dict_type(metadata, name)
        for k,v in metadata.items():
            self.__check_type(k, name)
            if not isinstance(v, list):
                raise TypeError('Values for metadata filtering must be a list.')
            for val in v:
                self.__check_type(val, name)
        return None


    def __check_literal(self, val: str, name: str=''):
        """Checks if input val is a valid value."""
        if not val in self.initial_storage.keys():
            raise ValueError(
                'The valid values are: '
                + str(self.initial_storage.keys())
                + 'Where: '
                + str(name)
            )

    def __add_op_tables(self, op_id, requests_storage):
        self.__check_type(op_id, 'OperacionTabla')
        tablas = self.SSM.INE.get_tables_(op_id)
        requests_storage['Tabla'][op_id] = tablas
        return requests_storage

    def __add_op_vars(self, op_id, requests_storage):
        self.__check_type(op_id, 'OperacionVariable')
        variables = self.SSM.INE.get_variables_(op_id)
        requests_storage['Variable'][op_id] = variables
        return requests_storage

    def __add_var_vals(self, var_id, requests_storage):
        self.__check_type(var_id, 'VariableValor')
        valores = self.SSM.INE.get_values_(var_id)
        requests_storage['Valor'][var_id] = valores
        return requests_storage

    def get_series(self, filtering_dict):
        self.__check_dict_type(filtering_dict, 'Series')
        op = filtering_dict.get('Operacion', None)
        tab = filtering_dict.get('Tabla', None)
        metadata_filter = filtering_dict.get('MetadataFiltering', None)

        if metadata_filter is None:
            return list(), None
        is_empty = not bool(metadata_filter)
        if is_empty and tab is None:
            return list(), None

        if tab is not None:
            self.__check_type(tab, 'Operacion Tabla')
            series = self.SSM.INE.get_series_(tab_id=tab,
                                              metadata_filtering=metadata_filter)
        else:
            self.__check_type(op, 'Operacion Serie')
            self.__check_metadata_filter(metadata_filter, 'Metadata filters Serie')
            series = self.SSM.INE.get_series_(op_id=op,
                                              metadata_filtering=metadata_filter)

        metadata_str = ''
        for var, val_list in metadata_filter.items():
            metadata_str += f'var:{var}val:{str(val_list)}'
        store_str = f'op:{op}tab:{tab}vvp:{metadata_str}'
        return series, store_str

    def get_obj(self, obj_type: str, obj_depend: int, requests_storage):
        """
        Gets the requested INE objects. Makes the request if it hadn't.

        Parameters
        ----------
        obj_type : Literal['Tabla' | 'Variable' | 'Valor' | 'Periodo']
            INE Objects to retreive.
        obj_depend : int
            INE obj ID that it depended on.
                * OP for Tabla and Variable.
                * Var for Valor
        requests_storage : Type
            The session storage.

        Returns
        -------
        data : Tuple[List of INE objects, requests_storage]
            Tuple with the requested data and the updated requests_storage
        requests_storage: Type
            The same session_storage with the updated values.

        """
        if obj_type in ['Operaciones', 'Publicaciones',
                        'Escalas', 'Unidades', 'Periodicidades']:
            return requests_storage.get(obj_type)

        self.__check_type(obj_depend, 'Getting requested INE objects.')
        self.__check_literal(obj_type, 'Getting requested INE objects.')

        data = requests_storage.get(obj_type).get(obj_depend, None)

        if data is None:
            if obj_type == 'Tabla':
                requests_storage = self.__add_op_tables(
                    obj_depend,
                    requests_storage
                )
            elif obj_type == 'Variable':
                requests_storage = self.__add_op_vars(
                    obj_depend,
                    requests_storage
                )
            elif obj_type == 'Valor':
                requests_storage = self.__add_var_vals(
                    obj_depend,
                    requests_storage
                )
            elif obj_type == 'Serie':
                requests_storage = self.__add_series(obj_depend,
                                                     requests_storage)
            elif obj_type in ['Periodo', 'Data']:
                raise ValueError('Pendiente de actualizar.')

            data = requests_storage.get(obj_type).get(obj_depend, None)
        return data, requests_storage

    def get_object_loop(self,
                        obj_type_list: list, obj_depend_list: list,
                        requests_storage):
        """
        Makes a requests for each obj_type and stores the result. Returns the storage.

        Parameters
        ----------
        obj_type : list
            The values must be same as get_obj method
        obj_depend : list
            The values must be same as get_obj method
        requests_storage : TYPE
            The requests storage to update.

        Returns
        -------
        requests_storage : TYPE
            The requests storage, updated.

        """
        if not isinstance(obj_type_list, list):
            raise TypeError('obj_type_list must be a list.')

        if not isinstance(obj_depend_list, list):
            raise TypeError('obj_depend_list must be a list.')

        if len(obj_type_list) != len(obj_depend_list):
            raise ValueError('Both list must be of the same length.')

        for obj_type, obj_depend in zip(obj_type_list, obj_depend_list, strict=True):
            _, requests_storage = self.get_obj(obj_type, obj_depend, requests_storage)
        return requests_storage


    # End of class









