# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 16:05:53 2025

@author: mano
"""

from dash import dcc
from Components.Storage.SingletonCustom import SingletonMeta

"""
The Dummy Storage is a storage used to store if some processes has been done
or not in order to allow some other process to execute.

Since dash uses consecutive Inputs updates to chain callbacks,
but doesn't allow define multiple callbacks that depend on one input and
specify the callback chain. This class allows to manage the session storage
instance aswell as a bunch of methods that will allow the functions to check
if they need to be executed or not.
"""

class DummyStorageManager(metaclass=SingletonMeta):

    def __init__(self):
        self.__default_value = -1
        # -1 Por que si usamos None dará error al hacer la comprobación.
        return None

    def get_initial_storage(self, storage_num=None):
        if storage_num is None:
            storage_num = ''
        storage = dcc.Store('DummyStorage' + str(storage_num), 'session',
                            data={'last_update': self.__default_value})
        return storage

    def add_update(self, name, dummy_storage):
        dummy_storage['last_update'] = name
        return dummy_storage

    def get_last_update(self, dummy_storage):
        return dummy_storage['last_update']

    def namer(self, select_name, row_lv1, row_lv2=None):
        text = str(select_name)
        if row_lv1 is not None:
            text = text + '_' + str(row_lv1)
        if row_lv2 is not None:
            text = text + '_' + str(row_lv2)
        return text

    def reset_default_value(self, dummy_storage):
        dummy_storage['last_update'] = self.__default_value
        return dummy_storage

    def get_default_value(self):
        return self.__default_value