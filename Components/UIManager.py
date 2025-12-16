# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 14:27:27 2025

@author: mano
"""

from dash import html
from Components.Storage.SingletonCustom import SingletonMeta
from Components.UIComponents.Common.Styles import MAIN_LAYOUT_STYLE

"""
This module contains the class that allows to manage the events that will
happen when the user interacts with the interface.
"""


"""
UIManager handles the UI transformations depending on user inputs.

This means that it is this class which takes care of applying the event
listeners to the UI components aswell as transforming the layout.
"""
class UIManager(metaclass=SingletonMeta):
    """Provides methods to manage the UI different states."""
    def __init__(self):

        return None

    def make_initial_layout(self):
        layout = html.Div(
            children = [],
            style = MAIN_LAYOUT_STYLE
        )
        return layout























