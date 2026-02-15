# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 13:11:57 2026

@author: mano
"""


from dash import html
from Components.UIComponents.Managers.UIManager import UIManager

from Components.UIComponents.Common.SelectComponent import SelectComponent

UIM = UIManager()

def ReloadDataButton():
    comp = html.Button(
        children=[
            html.Div('', className='svg reload'),
            html.Span('Recargar Series')
        ],
        className='btn-refresh-table',
        **{'id': UIM.id_generator('Input', 'Recargar Series', 'Button')}
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
        'Operación (COD)',
        'Serie',
        'Grafica',
        'Eje Grafica'
    ]
    cells = [Cell(col) for col in cols]
    comp = html.Div(
        children=cells,
        className='table-row header-row'
    )
    return comp


def SelectedCheck(serie_id, row_lv1):
    comp = html.Div(
        children='',
        className='svg circle check-icon row-checkbox',
        **{'id': UIM.id_generator('Input', 'Serie', 'Checkbox', row_lv1),
           'data-checked': "0",
           'data-serie-id': serie_id}
    )
    return comp

def SelectGrafica(row_lv1):
    options = [{'Id': 1}]
    comp = SelectComponent(options, 'Grafica', row_lv1, only_id=True)
    return comp

def SelectGraficaAxis(row_lv1):
    options = [{'Id': 1}, {'Id': 2}]
    comp = SelectComponent(options, 'Eje Grafica', row_lv1, only_id=True)
    return comp

def serie_data_to_row(serie_data, row_lv1):
    data = [
        serie_data['FK_Operacion'],
        serie_data['Nombre'],
        SelectGrafica(row_lv1),
        SelectGraficaAxis(row_lv1),
    ]

    cells = [Cell(d) for d in data]

    row = html.Div(
        children=cells,
        className='table-row data-row',
        **{'id': UIM.id_generator('Label', 'Serie', 'Row', row_lv1),
           'data-checked': "0",
           'data-serie-id': serie_data['Id']}
    )
    return row

def TableOptions(list_of_series):
    childs = [serie_data_to_row(data, i + 1) for i, data in enumerate(list_of_series)]
    return childs


def TableContainer():
    comp = html.Div(
        children=[
            TableHeader(),
            *TableOptions([])
        ],
        className='custom-table-container',
        **{'id': UIM.id_generator('Container', 'Table')}
    )
    return comp