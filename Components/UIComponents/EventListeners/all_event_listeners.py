# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 18:02:56 2026

@author: mano
"""

from Components.UIComponents.EventListeners.ClientsideListeners.store_selected_input import store_input_to_state_event_listener
from Components.UIComponents.EventListeners.ClientsideListeners.add_options import add_options_event_listener
from Components.UIComponents.EventListeners.ClientsideListeners.check_requested import check_requested_event_listener
from Components.UIComponents.EventListeners.ClientsideListeners.sidebar_toggle import add_sidebar_toggle_event_listener
from Components.UIComponents.EventListeners.ClientsideListeners.light_dark_switch import add_light_dark_event_listener
from Components.UIComponents.EventListeners.ClientsideListeners.add_remove_row import update_row_event_listener
from Components.UIComponents.EventListeners.ClientsideListeners.enable_buttons import enable_buttons_event_listener
from Components.UIComponents.EventListeners.ClientsideListeners.select_serie_switch import select_serie_event_listener
from Components.UIComponents.EventListeners.ClientsideListeners.add_series_to_table import add_series_event_listener
from Components.UIComponents.EventListeners.ClientsideListeners.plot_data import plot_graph_event_listener

from Components.UIComponents.EventListeners.ServersideListeners.data_gatherer import data_request_event_listener_adder


def add_event_listeners():
    # Clientside
    update_row_event_listener()
    enable_buttons_event_listener()
    store_input_to_state_event_listener()
    add_options_event_listener()
    check_requested_event_listener()
    add_sidebar_toggle_event_listener()
    add_light_dark_event_listener()
    select_serie_event_listener()
    add_series_event_listener()
    plot_graph_event_listener()

    # Serverside
    data_request_event_listener_adder()
    return None