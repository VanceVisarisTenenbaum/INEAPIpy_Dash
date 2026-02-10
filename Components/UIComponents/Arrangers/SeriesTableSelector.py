# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 13:11:57 2026

@author: mano
"""


from dash import html


def ReloadDataButton():
    comp = html.Button(
        children=[
            html.Div('', className='svg reload'),
            html.Span('Recargar Series')
        ],
        className='btn-refresh-table',
        **{'id': 'Botón Recargar'}
    )
    return comp



def TableTitle():
    comp = html.Div(
        children=[
            html.H3('Series', className='table-title'),
            ReloadDataButton()
        ],
        className='table-title-header'
    )
    return comp


def Cell(data):
    comp = html.Div(
        children=data,
        className='cell'
    )
    return comp

def TableHeader():
    cols = [
        '#'
        'Operación (COD)',
        'Serie',
        'Periodicidad',
        'Publicacion',
        'Clasificacion',
        'Escala',
        'Unidad',
    ]
    cells = [Cell(col) for col in cols]
    comp = html.Div(
        children=cells,
        className='table-row header-row'
    )
    return comp