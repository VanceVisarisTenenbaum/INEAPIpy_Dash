# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 17:00:58 2025

@author: mano
"""

SELECT_INPUT_STYLE = {
    'width': '90%',
    'height': '100px',
    'fontSize': '15px'
}

LABEL_STYLE = {
    'width': '90%',
    'fontSize': '40px'
}

LABEL_INPUT_STYLE_COMMON = {
    'alignItems': 'left',
    'padding': '6px'
}

LABEL_INPUT_STYLE_TOP = dict(LABEL_INPUT_STYLE_COMMON)
LABEL_INPUT_STYLE_TOP.update({
    'display': 'flex',
    'flexDirection': 'column'
})

LABEL_INPUT_STYLE_SIDE = dict(LABEL_INPUT_STYLE_COMMON)
LABEL_INPUT_STYLE_SIDE.update({
    'display': 'block'
})

ROW_SEPARATED_DIVS_BASE = {
    "display": "flex",
    "flexDirection": "column",
    "width": "100%",
    "overflowY": "auto",        # Scroll vertical si hay overflow
    "gap": '10px'
}

ROW_SEPARATED_DIVS = {
    "maxHeight": "25%",       # Altura máxima de 1/4 el del padre
    "border": "1px solid #ccc",
    "padding": "10px",
}
ROW_SEPARATED_DIVS.update(ROW_SEPARATED_DIVS_BASE)

INPUT_SELECTION_BOX_STYLE = {
    "maxHeight": "90%",
    "minHeight": "80%",
    "padding": "0px",
}
INPUT_SELECTION_BOX_STYLE.update(ROW_SEPARATED_DIVS_BASE)

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
    'fontSize': '30px',
    'fontWeight': 'bold',
}

SPAN_INFO_VALUE_STYLE = {
    'fontSize': '25px',
}

NAME_VALUE_DISPLAY_STYLE = {
    'height': '35%'
}

NAME_VALUE_DISPLAY_GRID_STYLE = {
    'display': 'grid',
    'gridTemplateColumns': 'repeat(2, 1fr)',
    'gap': '16px',
    'maxHeight': '50%',
    'overflowY': 'auto'
}

