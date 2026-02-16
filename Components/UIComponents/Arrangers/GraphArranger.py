# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 16:08:04 2026

@author: mano
"""

from dash import html

from Components.UIComponents.Managers.UIManager import UIManager


UIM = UIManager()

def ReloadDataButton():
    comp = html.Button(
        children=[
            html.Div('', className='svg reload'),
            html.Span('Recargar Datos')
        ],
        className='btn-refresh-table',
        **{'id': UIM.id_generator('Input', 'Recargar Datos', 'Button')}
    )
    return comp


def GraphTitle():
    comp = html.Div(
        children=[
            html.H3('Gráficas', className='table-title'),
            ReloadDataButton()
        ],
        className='table-title-header'
    )
    return comp

def GraphContainer():
    comp = html.Div(
        children=[
            html.Div(
                children=[],
                className='charts-grid-layout',
                **{'id': UIM.id_generator('Container', 'Graphs')}
            )
        ],
        className='charts-scroll-area',
        **{'id': UIM.id_generator('Container', 'Graphs', 'Box')}
    )
    return comp
