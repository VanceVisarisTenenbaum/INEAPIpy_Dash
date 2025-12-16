# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 17:21:08 2025

@author: mano
"""

"""
The UI Components follow a defined convention, in order to maintain the
convention in the app we define a function that returns the expected ID
for any component.

The UI is composed as follows:
-
Input Selections Box
    Inputs Group Row 1
    Inputs Group Row 2
    ...
        Operation Selection Box
            -- Label Operacion
            -- Select Operacion
        Table Selection Box
            -- Label Tabla
            -- Select Tabla
        Variable Value Selection Box
            Variable Valor Row 1
            Variable Valor Row 2
            ...
                Variable Selection Box
                    -- Label Variable
                    -- Select Variable
                Valor Selection Box
                    -- Label Valor
                    -- Select Valor
        Load Series Button
        Serie Selection Box
            -- Label Series
            -- MultiSelect Series
            -- Select Gráfica
            -- Select Eje
            -- Select Estilo
Graph Display Box
    Graph Display 1
    Graph Display 2
    ...
        -- Label Gráfica
        -- Display Gráfica

-------------------------------------------------------------------------------

The naming convention is as follows:
-
Input Selection Box ---------> ISB
Inputs Group ----------------> IG_i  <------ where "i" is the row number

Operation Select Box --------> OperacionBox_i
    Label Operacion ---------> OperacionLabel_i
    Select Operacion --------> Operacion_i

Table Select Box ------------> TablaBox_i
    Label Tabla -------------> TablaLabel_i
    Select Tabla ------------> Tabla_i

Variable Valor Box ----------> VariableValorBox_i
    Variable Valor ----------> VariableValor_i_k <- where "k" is the row number
        Variable Box --------> VariableBox_i_k
            Label Variable --> VariableLabel_i_k
            Select Variable -> Variable_i_k
        Valor Box -----------> ValorBox_i_k
            Label Valor -----> ValorLabel_i_k
            Select Valor ----> Valor_i_k

Graph Display Box -----------> GDB
Graph Display ---------------> GD_j <------ where "j" is the row number
    Label Grafica j ---------> GraficaLabel_j
    Grafica -----------------> Grafica_j


La convención se puede simplificar en los siguientes parámetros:
    Nombre, Tipo[Opcional], Fila_Nivel_1[Opcional], Fila_Nivel_2[Opcional]

    Nombre es el nombre que quieres darle al componente UI
    Tipo, si es un Box, Label o nada.
    Fila_Nivel_1, está claro.
    Fila_Nivel_2, está claro.
"""

def id_generator(nombre: str, tipo: str=None,
                 fila_lv1: int=None, fila_lv2: int= None):
    id_name = str(nombre)
    if tipo is not None:
        id_name = id_name + str(tipo)
    if fila_lv1 is not None:
        id_name = id_name + '_' + str(fila_lv1)
    if fila_lv2 is not None:
        id_name = id_name + '_' + str(fila_lv2)

    return id_name


"""
Since we will need to use the same name in different files of the code
we use a simple mapper that simplifies the name transformations using some
short terms.
"""

def name_mapper(short_name):
    map_dict = {
        'O': 'Operacion',
        'T': 'Tabla',
        'Vr': 'Variable',
        'Vl': 'Valor',
        'G': 'Grafica',
    }
    long_name = map_dict.get(short_name, short_name)
    # returns the same if it is not found.
    return long_name

def id_generator_mapper(nombre: str, tipo: str=None,
                        fila_lv1: int=None, fila_lv2: int= None):
    return id_generator(name_mapper(nombre), tipo, fila_lv1, fila_lv2)

