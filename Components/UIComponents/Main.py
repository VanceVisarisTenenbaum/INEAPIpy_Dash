# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 16:40:05 2025

@author: mano
"""

from dash import html, dcc

from Components.UIComponents.Managers.UIManager import UIManager

from Components.Storage.RequestsStorage import RequestsStorageManager
from Components.Storage.StateStorage import StateStorageManager
from Components.Storage.DummyStorage import DummyStorageManager

from Components.UIComponents.EventListeners.all_event_listeners import add_event_listeners

from Components.UIComponents.Layouts.Body import Body

DSM = DummyStorageManager()
SSM = StateStorageManager()
RSM = RequestsStorageManager()

UIM = UIManager()

def initial_layout():
    layout = html.Div(
        children = [
            RSM.get_initial_requests_storage(),
            SSM.get_initial_state_storage(),
            DSM.get_initial_storage('Client'),  # Client is the dummy that activates client function
            DSM.get_initial_storage('Server'),  # Server is the dummy that activates server function
            DSM.get_initial_storage('Series'),  # Dummy that stores the requested series.
            DSM.get_initial_storage('Selected_Series'),  # Dummy that stores the selected series.
            dcc.Store(UIM.id_generator('Storage', 'Log'), 'session', data=[]),
            Body()
        ],
        **{'id': 'main'}
    )
    add_event_listeners()
    return layout
