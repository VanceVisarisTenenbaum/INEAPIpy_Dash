# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 13:18:13 2025

@author: mano
"""

"""
This file contains some variables that should be constants in the app, plus
some additional functions.
"""

from INEAPIpy import Wrapper as W
from dash import dcc, html

# Cargamos todas las variables que se mantendrán constantes mientras se este
# usando el servidor.

INE = W.EasyINEAPIClientSync(mode='py')

"""
La mayoría de los metadatos de la API del INE no se van a actualizar con
frecuencia, por lo que se pueden cargar inicialmente en el servidor que corre
la aplicación y minimizar el uso de la API del INE en caso de que se tengan
muchos usuarios recurrentes.
"""

SERVER_MEMORY = {
    'Operaciones': INE.get_operations_(),  # Menos de 200.
    'Publicaciones': INE.get_publications_(),  # Menos de 500.
    'Unidades': INE.get_units_(),
    'Escalas': INE.get_scales_(),
    'Periodicidades': INE.get_periodicities_()
}



