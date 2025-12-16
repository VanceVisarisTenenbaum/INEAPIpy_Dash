# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 11:42:39 2025

@author: mano
"""

from dash import dcc
from Components.Storage.SingletonCustom import SingletonMeta
from Components.Storage.ServerMemory import ServerMemoryManager

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
            'Periodo': dict()
        }

        SESSION_STORAGE = dcc.Store(**{'id': 'SessionStorage',
                                       'storage_type': 'session'},
                                    data=self.initial_storage)
        self.__initial_session_storage = SESSION_STORAGE
        return None

    def get_initial_requests_storage(self):
        return self.__initial_session_storage

    def __check_type(self, val: int, name: str=''):
        """Checks if the input was an int. Name is for debugging."""
        if not isinstance(val, int):
            raise TypeError('Input is not an int. Where: ' + str(name))
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

    def __add_op_tables(self, op_id, session_storage):
        self.__check_type(op_id, 'OperacionTabla')
        tablas = self.SSM.INE.get_tables_(op_id)
        session_storage['Tabla'][op_id] = tablas
        return session_storage

    def __add_op_vars(self, op_id, session_storage):
        self.__check_type(op_id, 'OperacionVariable')
        variables = self.SSM.INE.get_variables_(op_id)
        session_storage['Variable'][op_id] = variables
        return session_storage

    def __add_var_vals(self, var_id, session_storage):
        self.__check_type(var_id, 'VariableValor')
        valores = self.SSM.INE.get_values_(var_id)
        session_storage['Valor'][var_id] = valores
        return session_storage

    def get_obj(self, obj_type: str, obj_depend: int, session_storage):
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
        session_storage : Type
            The session storage.

        Returns
        -------
        data : Tuple[List of INE objects, session_storage]
            Tuple with the requested data and the updated session_storage

        """
        self.__check_type(obj_depend, int, 'Getting requested INE objects.')
        self.__check_literal(obj_type, 'Getting requested INE objects.')

        data = session_storage.get(obj_type).get(obj_depend, None)

        if data is None:
            if obj_type == 'Tabla':
                session_storage = self.__add_op_tables(
                    obj_depend,
                    session_storage
                )
            elif obj_type == 'Variable':
                session_storage = self.__add_op_vars(
                    obj_depend,
                    session_storage
                )
            elif obj_type == 'Valor':
                session_storage = self.__add_var_vals(
                    obj_depend,
                    session_storage
                )
            elif obj_type == 'Periodo':
                raise ValueError('Pendiente de actualizar.')

        data = session_storage.get(obj_type).get(obj_depend, None)
        return data, session_storage








