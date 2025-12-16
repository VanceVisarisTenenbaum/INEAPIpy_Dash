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

    def __check_literal__(self, val):
        if val not in self.__SERVER_MEMORY.keys():
            raise ValueError('The input value is not in server memory keys.')
        return None

    def get_metadata(self, ine_obj: str, ine_id: int = None):
        self.__check_literal__(ine_obj)
        if ine_id is None:
            return self.__SERVER_MEMORY[ine_obj]
        return next(
            (x for x in self.__SERVER_MEMORY[ine_obj] if x['Id'] == ine_id),
            None
        )

