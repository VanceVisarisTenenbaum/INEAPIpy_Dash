# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 22:34:29 2026

@author: mano
"""

from Components.Storage.SingletonCustom import SingletonMeta

class NameManager(metaclass=SingletonMeta):
    """Class that takes care of Id names for components"""
    def __init__(self):
        return None
    # End of class