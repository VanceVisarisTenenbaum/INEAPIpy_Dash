# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 16:40:05 2025

@author: mano
"""

from dash import html
from Components.UIComponents.Arrangers.InputsBox import (InputSelectionBox, make_IGR)

from Components.UIComponents.Managers.UIManager import UIManager

from Components.Storage.RequestsStorage import RequestsStorageManager
from Components.Storage.StateStorage import StateStorageManager
from Components.Storage.DummyStorage import DummyStorageManager

from Components.UIComponents.EventListeners.all_event_listeners import add_event_listeners

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
            InputSelectionBox(make_IGR(1))
        ],
        **{'id': 'main'}
    )
    add_event_listeners()
    return layout
