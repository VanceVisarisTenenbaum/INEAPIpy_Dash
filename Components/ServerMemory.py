# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 17:12:51 2025

@author: mano
"""

from INEAPIpy import Wrapper as W

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


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