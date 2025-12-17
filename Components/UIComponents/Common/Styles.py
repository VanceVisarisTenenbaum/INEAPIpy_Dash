# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 17:00:58 2025

@author: mano
"""

SELECT_INPUT_STYLE = {
    'width': '90%',
    'height': '100px',
    'font-size': '15px'
}

LABEL_STYLE = {
    'width': '90%',
    'font-size': '40px'
}

LABEL_INPUT_STYLE_COMMON = {
    'width': '100%',
    'alignItems': 'left',
    'padding': '6px'
}

LABEL_INPUT_STYLE_TOP = dict(LABEL_INPUT_STYLE_COMMON)
LABEL_INPUT_STYLE_TOP.update({
    'display': 'flex',
    'flex-direction': 'column'
})

LABEL_INPUT_STYLE_SIDE = dict(LABEL_INPUT_STYLE_COMMON)
LABEL_INPUT_STYLE_SIDE.update({
    'display': 'block'
})

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


SPAN_INFO_NAME_STYLE = {
    'font-size': '30px',
    'font-weight': 'bold',
}

SPAN_INFO_VALUE_STYLE = {
    'font-size': '25px',
}

NAME_VALUE_DISPLAY_STYLE = {
    'height': '35%'
}

NAME_VALUE_DISPLAY_GRID_STYLE = {
    'display': 'grid',
    'grid-template-columns': 'repeat(2, 1fr)',
    'gap': '16px',
    'maxHeight': '50%',
    'overflowY': 'auto'
}

