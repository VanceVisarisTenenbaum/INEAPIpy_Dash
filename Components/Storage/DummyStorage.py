# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 16:05:53 2025

@author: mano
"""

from dash import dcc

"""
The Dummy Storage is a storage used to store if some processes has been done
or not in order to allow some other process to execute.

Since dash uses consecutive Inputs updates to chain callbacks,
but doesn't allow define multiple callbacks that depend on one input and
specify the callback chain. This class allows to manage the session storage
instance aswell as a bunch of methods that will allow the functions to check
if they need to be executed or not.
"""