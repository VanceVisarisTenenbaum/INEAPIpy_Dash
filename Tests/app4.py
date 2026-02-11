# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 15:15:18 2026

@author: mano
"""


from dash import html, Dash



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

def serie_data_to_row(serie_data):
    data = [
        serie_data['Operacion'],
        serie_data['Nombre'],
        serie_data['Periodicidad'],
        serie_data['Publicacion'],
        serie_data['Clasificacion'],
        serie_data['Escala'],
        serie_data['Unidad'],
    ]
    cells = [Cell(d) for d in data]
    row = html.Label(
        children=cells,
        className='table-row data-row'
    )
    return row

def serie_data_to_option(serie_data):
    option = {
        'label': serie_data_to_row(serie_data),
        'value': serie_data['Id']
    }
    return option

def TableOptions(list_of_series):

    comp = [serie_data_to_row(data) for data in list_of_series]


    return comp

sample_series = [
    {"Operacion": 1,  "Nombre": 2,  "Periodicidad": 3,  "Publicacion": 4,  "Clasificacion": 5,  "Escala": 6,  "Unidad": 7, "Id": 20},
    {"Operacion": 8,  "Nombre": 9,  "Periodicidad": 10, "Publicacion": 11, "Clasificacion": 12, "Escala": 13, "Unidad": 14, "Id": 21},
    {"Operacion": 15, "Nombre": 16, "Periodicidad": 17, "Publicacion": 18, "Clasificacion": 19, "Escala": 20, "Unidad": 21, "Id": 22},
    {"Operacion": 22, "Nombre": 23, "Periodicidad": 24, "Publicacion": 25, "Clasificacion": 26, "Escala": 27, "Unidad": 28, "Id": 23},
    {"Operacion": 29, "Nombre": 30, "Periodicidad": 31, "Publicacion": 32, "Clasificacion": 33, "Escala": 34, "Unidad": 35, "Id": 24},
    {"Operacion": 36, "Nombre": 37, "Periodicidad": 38, "Publicacion": 39, "Clasificacion": 40, "Escala": 41, "Unidad": 42, "Id": 25},
    {"Operacion": 43, "Nombre": 44, "Periodicidad": 45, "Publicacion": 46, "Clasificacion": 47, "Escala": 48, "Unidad": 49, "Id": 26},
    {"Operacion": 50, "Nombre": 51, "Periodicidad": 52, "Publicacion": 53, "Clasificacion": 54, "Escala": 55, "Unidad": 56, "Id": 27},
    {"Operacion": 57, "Nombre": 58, "Periodicidad": 59, "Publicacion": 60, "Clasificacion": 61, "Escala": 62, "Unidad": 63, "Id": 28},
    {"Operacion": 64, "Nombre": 65, "Periodicidad": 66, "Publicacion": 67, "Clasificacion": 68, "Escala": 69, "Unidad": 70, "Id": 29}
]

def TableContainer():
    comp = html.Div(
        children=[
            TableHeader(),
            TableOptions(sample_series)
        ],
        className='custom-table-container'
    )
    return comp

def main():
    """Starts the App."""


    """Iniciamos el servidor de dash."""
    app = Dash(__name__, assets_folder='../assets')

    app.layout = html.Div(
        children=[
            TableTitle(),
            TableContainer()
        ]
    )
    app.run(debug=True)
    return None




if __name__ == '__main__':
    main()