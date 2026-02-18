# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 16:08:48 2026

@author: mano
"""

from dash import callback, ctx, no_update, Patch

from Components.Storage.RequestsStorage import RequestsStorageManager
from Components.Storage.StateStorage import StateStorageManager
from Components.Storage.DummyStorage import DummyStorageManager

from Components.UIComponents.Managers.UIManager import UIManager


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

UIM = UIManager()
def data_requesting_maker():
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


    input_type_to_request_type_map = { # Map of "what I select to what i need"
        'Operacion': ['Variable', 'Tabla'],  # Select an Operation, so I need to get the
        'Variable': ['Valor'],
        # 'Tabla': ['Serie'],  # Las series se obtienen utilizando un botón
        'Serie': ['Data']
    }
    def request_process(input_name, input_value,
                        requests_storage):

        obj_type = input_type_to_request_type_map[input_name]
        obj_depend = [input_value for _ in obj_type]
        # Same value for each object to request.
        requests_storage = RSM.get_object_loop(obj_type,
                                               obj_depend,
                                               requests_storage)

        return requests_storage

    # El event listener espera que el dummy tenga el valor elegido.
    @callback(
        inputs=[
            UIM.io_generator('Input', 'data',
                             ui_type='Storage',
                             ui_name='Dummy',
                             ui_subtype='Server'),
        ],
        state=[
            UIM.io_generator('State', 'data',
                             ui_type='Storage',
                             ui_name='Requests'),
            UIM.io_generator('State', 'data',
                             ui_type='Storage',
                             ui_name='Dummy',
                             ui_subtype='Client'),
        ],
        output=[
            UIM.io_generator('Output', 'data',
                             ui_type='Storage',
                             ui_name='Dummy',
                             ui_subtype='Server',
                             allow_duplicate=True),
            UIM.io_generator('Output', 'data',
                             ui_type='Storage',
                             ui_name='Requests'),
            UIM.io_generator('Output', 'data',
                             ui_type='Storage',
                             ui_name='Dummy',
                             ui_subtype='Client',
                             allow_duplicate=True),
        ],
        prevent_initial_call=True
    )
    def normal_request(server_dummy_storage, requests_storage, client_dummy_storage):
        input_ = DSM.get_last_update(server_dummy_storage)
        server_dummy_storage = DSM.reset_default_value(server_dummy_storage)

        input_type = input_['Input Type']
        input_val = input_['Valor']
        requests_storage = request_process(input_type, input_val,
                                           requests_storage)

        client_dummy_storage = DSM.add_update(
            input_,
            client_dummy_storage
        )
        return server_dummy_storage, requests_storage, client_dummy_storage

    #añadir event listener botón series
    def load_series(state_storage):

        list_of_series = list()
        for row_lv1, data in state_storage.items():
            op = data['Operacion']
            tab = data['Tabla']
            metadata_filtering = dict()
            for row_lv2, vvp in data['VariableValor'].items():
                lista_valores = metadata_filtering.get(vvp['Variable'], None)
                if lista_valores is None:
                    metadata_filtering[vvp['Variable']] = list()
                metadata_filtering[vvp['Variable']].append(vvp['Valor'])

            metadata_filter = {
                'Operacion': op,
                'Tabla': tab,
                'MetadataFiltering': metadata_filtering
            }
            series, _ = RSM.get_series(metadata_filter)
            list_of_series.extend(series)

        return list_of_series

    @callback(
        inputs=UIM.io_generator(
            'Input', 'n_clicks',
            ui_type='Input',
            ui_name='Recargar Series',
            ui_subtype='Button'
        ),
        state=UIM.io_generator(
            'State', 'data',
            ui_type='Storage',
            ui_name='State'
        ),
        output=UIM.io_generator(
            'Output', 'data',
            ui_type='Storage',
            ui_name='Dummy',
            ui_subtype='Series'
        ),
        prevent_initial_call=True
    )
    def serie_request(n_clicks, state_storage):
        if n_clicks == 0:
            return None
        series = load_series(state_storage)
        return series


    def load_data(series_id_list):
        return RSM.get_data(series_id_list)


    @callback(
        inputs=UIM.io_generator(
            'Input', 'n_clicks',
            ui_type='Input',
            ui_name='Recargar Datos',
            ui_subtype='Button'
        ),
        state=UIM.io_generator(
            'State', 'data',
            ui_type='Storage',
            ui_name='Dummy',
            ui_subtype='Selected_Series'
        ),
        output=UIM.io_generator(
            'Output', 'data',
            ui_type='Storage',
            ui_name='Dummy',
            ui_subtype='Requested_Data'
        ),
        prevent_initial_call=True
    )
    def data_requests(n_clicks, selected_series_storage):
        if isinstance(selected_series_storage, dict):
            new_data = list()
        else:
            new_data = load_data(selected_series_storage)
        patch = Patch()
        patch['last_update'] = new_data
        return patch

    return None

def data_request_event_listener_adder():
    data_requesting_maker()
    return None