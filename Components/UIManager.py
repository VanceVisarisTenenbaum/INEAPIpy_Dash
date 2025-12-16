# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 14:27:27 2025

@author: mano
"""

from Components.Storage.SingletonCustom import SingletonMeta

"""
This module contains the class that allows to manage the events that will
happen when the user interacts with the interface.

The UI is composed as follows.

Inputs Selection Box
    Operation Selection
    Table Selection
    VarVal Selection Box
        Variable Selection
        Value Selection
    Serie Selection
        Graph Selection
        Axis Selection
        Style Selection
Graph Display Box
    Graph 1
    Graph 2
    .
    .
    .

The UI allows to selecte multiple Operations and for each operation you can
select 1 table, multiple var value pairs. and multiple series.

To add the event listeners it is required to specify the IDs to each component
in order to do so the next naming convention is adopted.

Input Selection Box --> InputsBox
    Row RN --> 'InputsBox_RN'
        OperationSelect --> Operation_RN
        TableSelect --> Table_RN -------------- Should only appear when
                                                operation is selected.
        VarValBox --> VarValBox_RN ------------ Same as TableSelect
            VarValRow VVRN --> VarVal_RN_VVRN
                Variable Select --> VarSelect_RN_VVRN
                Value Select --> ValSelect_RN_VVRN
        SerieBox --> SerieBox_RN
            SerieMultiSelect --> SerieMSelect_RN
            GraphDisplaySelectBox --> GraphDSBox_RN
                SelectedSerieBox SSID --> SelectedSerieBox_RN_SSID
                    SelectedSerieSpan --> SSSpan_RN_SSID
                    GraphSelect --> GS_RN_SSID
                    AxisSelect --> AS_RN_SSID
                    StyleSelect --> SS_RN_SSID

Graph Display Box --> GraphBox
    GraphDisplayBox GDB --> GraphDisplay_GDB
        GraphIDSpan --> GSpan_GDB
        Graph --> Graph_GDB
"""


class UIManager(metaclass=SingletonMeta):
    """Provides methods to manage the UI different states."""
    def __init__(self):
        return None





















