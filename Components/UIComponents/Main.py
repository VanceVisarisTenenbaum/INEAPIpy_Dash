# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 16:40:05 2025

@author: mano
"""

from dash import html
from Components.UIComponents.SelectionBox import InputSelectionBox
from Components.UIComponents.OperationBox import (operation_event_listener_adder,
                                                  make_row)

from Components.Storage.RequestsStorage import RequestsStorageManager
from Components.Storage.StateStorage import StateStorageManager
from Components.Storage.DummyStorage import DummyStorageManager

DSM = DummyStorageManager()
SSM = StateStorageManager()
RSM = RequestsStorageManager()

def initial_layout():
    layout = html.Div(
        children = [
            RSM.get_initial_requests_storage(),
            SSM.get_initial_state_storage(),
            DSM.get_initial_storage('OperacionClient'),  # Client is the dummy that activates client function
            DSM.get_initial_storage('OperacionServer'),  # Server is the dummy that activates server function
            DSM.get_initial_storage('VariableClient'),
            DSM.get_initial_storage('VariableServer'),
            InputSelectionBox(make_row(1))
        ],
        **{'id': 'main'}
    )
    operation_event_listener_adder()
    return layout
