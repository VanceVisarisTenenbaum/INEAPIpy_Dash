# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 17:00:58 2025

@author: mano
"""


COMMON_PADDING = '6px'

SELECT_INPUT_STYLE = {
    'width': '500px',
    'height': '100px',
    'padding': COMMON_PADDING
}

ROW_SEPARATED_DIVS = {
    "display": "flex",
    "flexDirection": "column",
    "overflowY": "auto",        # Scroll vertical si hay overflow
    "maxHeight": "25%",       # Altura máxima de 1/4 el del padre
    "width": "100%",
    "border": "1px solid #ccc",
    "padding": "10px",
    "gap": '10px'
}

COLUMN_SEPARATED_DIVS = {
    "display": "flex",
    "flexDirection": "row",
    "justifyContent": "center",
    "gap": "12px",  # Espacio fijo mínimo entre ellos
    "width": "100%"
}

MAIN_LAYOUT_STYLE = {
    "overflowY": "auto",
    'minHeight': "100%",
    'width': '100%'
}