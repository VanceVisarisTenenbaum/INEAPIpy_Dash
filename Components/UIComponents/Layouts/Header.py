# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 16:13:57 2026

@author: mano
"""

from dash import html, dcc


def ExportButton():
    comp = dcc.Button(
        children=[
            html.Div('', className='svg svg-download'),
            html.Span('Exportar como PNG')
        ],
        className='btn btn-secondary',
        **{'id': 'ExportButton'}
    )
    return comp

def HelpButton():
    comp = dcc.Button(
        children=[
            html.Div('', className='svg svg-help')
        ],
        className='icon-btn help-btn',
        **{'id': 'HelpButton'}
    )
    return comp

def LightDarkToggle():
    comp = html.Div(
        children=[
            html.Label(
                html.Div(
                    children=[
                        html.Span('', className='svg light'),
                        html.Span('', className='svg dark'),
                        html.Span('', className='svg switch-thumb')
                    ],
                    className='toggle-track'
                ),
                className='theme-toggle',
                htmlFor='light-dark-switch',
                **{'id':'light-dark-switch-label'}
            )
        ]
    )
    return comp


def SidebarToggle():
    comp = html.Label(
        children=html.Div('', className='svg hamburger-btn'),
        htmlFor='sidebar-toggle',
        className='hamburger-btn-label',
        style={'display': 'inline'},
        **{'id':'hamburger-btn-label'}
    )
    return comp

def Header():
    comp = html.Header(
        children=[
            html.Div(
                children=[
                    SidebarToggle(),
                    html.H1('Datos abiertos INE (no oficial)', className='header-title')
                ],
                className='header-left'
            ),
            html.Div(
                children=[
                    ExportButton(),
                    HelpButton(),
                    LightDarkToggle(),
                    html.P("""
Fuente de datos: www.ine.es
Licencia: Creative Commons Attribution 4.0 (CC BY 4.0).
Este sitio es un proyecto independiente y no oficial.
                    """)
                ],
                className='header-right'
            ),
        ],
        className='header'
    )
    return comp