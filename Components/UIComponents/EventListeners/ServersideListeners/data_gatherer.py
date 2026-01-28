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
de datos al INE y enviarlos al cliente.

El proceso consiste básicamente en definir el Input que activa la
obtención de datos, el output será siempre el request storage y
alguno de los posibles dummy que fuerzan la activación de los
event listeners del cliente.
"""

DSM = DummyStorageManager()
SSM = StateStorageManager()
RSM = RequestsStorageManager()


def data_requesting_maker(input_name):
    """
    Generates the callback that trigger the request of data to the INE API.

    Parameters
    ----------
    input_name : Literal['Operacion' | 'Variable' | 'Tabla' | 'Serie']
        The name of the Input that triggers the request of data.

    Returns
    -------
    None

    """
    dummy_server_name = str(input_name) + 'Server'
    dummy_client_name = str(input_name) + 'Client'


    input_type_to_request_type_map = { # Map of "what I select to what i need"
        'Operacion': ['Variable', 'Tabla'],  # Select an Operation, so I need to get the
        'Variable': ['Valor'],
        # 'Tabla': ['Serie'],  # Las series se obtienen utilizando un botón
        'Serie': ['Data']
    }
    def request_process(input_value, requests_storage,
                        client_dummy_storage):

        obj_type = input_type_to_request_type_map[input_name]
        obj_depend = [input_value for _ in obj_type]
        # Same value for each object to request.
        requests_storage = RSM.get_object_loop(input_value,
                                               obj_depend,
                                               requests_storage)

        client_dummy_storage = DSM.set_random_number(client_dummy_storage)

        return requests_storage, client_dummy_storage

    # El event listener espera que el dummy tenga el valor elegido.
    @callback(
        DUMMY_INPUT(dummy_server_name),
        STORAGE_INPUTS()[0], # Requests
        DUMMY_INPUT(dummy_client_name, True),
        DUMMY_OUTPUT(dummy_server_name),
        STORAGE_OUTPUTS()[0],
        DUMMY_OUTPUT(dummy_client_name),
        prevent_initial_call=True
    )
    def event_listener(server_dummy_storage, requests_storage, client_dummy_storage):
        input_val = DSM.get_last_update(server_dummy_storage)
        server_dummy_storage = DSM.reset_default_value(server_dummy_storage)
        requests_storage, client_dummy_storage = request_process(input_val,
                                                                 requests_storage,
                                                                 client_dummy_storage)


        return server_dummy_storage, requests_storage, client_dummy_storage

    # TODO, aladir event listener botón series

    return None

def data_request_event_listener_adder():
    data_requesting_maker('Operacion')
    data_requesting_maker('Variable')
    data_requesting_maker('Serie')
    return None