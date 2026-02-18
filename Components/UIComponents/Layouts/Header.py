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
    comp = html.A(
        children=[
            html.Div('', className='svg svg-help'),
            html.Span('Ayuda')
        ],
        href="https://github.com/VanceVisarisTenenbaum/INEAPIpy_Dash/blob/main/Documentaci%C3%B3n/ComoUsarLaAPP.md",
        target="_blank",
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
                    html.H1('Datos abiertos INE (no oficial)', className='header-title'),
                    HelpButton()
                ],
                className='header-left'
            ),
            html.Div(
                children=[
                    ExportButton(),
                    LightDarkToggle(),
                    html.Div(
                        children=[
                            html.P([html.Strong("Fuente de datos: "),
                                    html.A("www.ine.es",
                                           href="https://www.ine.es/",
                                           target="_blank",
                                           style={'color': "var(--text-primary)"})
                                    ]),
                            html.P([html.Strong("Licencia: "), "Creative Commons Attribution 4.0 (CC BY 4.0)."]),
                            html.P("Este sitio es un proyecto independiente y no oficial.")
                        ],
                        className="disclaimer"
                    )
                ],
                className='header-right'
            ),
        ],
        className='header'
    )
    return comp