# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 16:08:48 2026

@author: mano
"""

from dash import callback, ctx, no_update

from Components.Storage.RequestsStorage import RequestsStorageManager
from Components.Storage.StateStorage import StateStorageManager
from Components.Storage.DummyStorage import DummyStorageManager

from Components.UIComponents.Common.ui_processes import (STORAGE_INPUTS,
                                                         STORAGE_OUTPUTS,
                                                         DUMMY_INPUT,
                                                         DUMMY_OUTPUT,
                                                         io_generator)


"""
El servidor se encarga únicamente de realizar las solicitudes
de datos al INE y enviarlos al usuario.

El proceso consiste básicamente en definir el Input que activa la
obtención de datos, el output será siempre el request storage y
alguno de los posibles dummy que fuerzan la activación de los
event listeners del cliente.
"""

DSM = DummyStorageManager()
SSM = StateStorageManager()
RSM = RequestsStorageManager()


def data_gatherer_maker(input_name, dash_input, dummy_output):


    @callback(

    )
    def op_process(server_dummy_storage,
                   input_val, requests_storage,
                   client_dummy_storage):



        return requests_storage, client_dummy_storage

    return None