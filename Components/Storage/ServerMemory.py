# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 17:12:51 2025

@author: mano
"""

from INEAPIpy import Wrapper as W
from Components.Storage.SingletonCustom import SingletonMeta


class ServerMemoryManager(metaclass=SingletonMeta):

    def __init__(self):
        """Definimos el cache del server"""

        self.INE = W.EasyINEAPIClientSync(mode='py', print_url=True)

        """
        La mayoría de los metadatos de la API del INE no se van a actualizar con
        frecuencia, por lo que se pueden cargar inicialmente en el servidor que corre
        la aplicación y minimizar el uso de la API del INE en caso de que se tengan
        muchos usuarios recurrentes.
        """

        self.__SERVER_MEMORY = {
            'Operaciones': self.INE.get_operations_(),  # Menos de 200.
            'Publicaciones': self.INE.get_publications_(),  # Menos de 500.
            'Unidades': self.INE.get_units_(),
            'Escalas': self.INE.get_scales_(),
            'Periodicidades': self.INE.get_periodicities_()
        }

    def get_server_memory(self):
        return self.__SERVER_MEMORY