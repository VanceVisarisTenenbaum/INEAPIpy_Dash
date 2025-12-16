# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 17:20:54 2025

@author: mano
"""

from dash import Dash, html, dcc
import Components.SelectionBox as SB


def main():
    """Starts the App."""


    initial_state = dict()
    STATE_STORAGE = dcc.Store(**{'id': 'StateStorage',
                                 'storage_type': 'session'},
                              data=initial_state)
    """
    State Storage is meant to store in session all the decisions made by
    the user. Given this the shape of the dictionary should match
    the shape of the selection process. This is:
        1. There are multiple Operation selection boxes
        2. For each OperationBox
            * There is 0 or 1 table selected.
            * There are multiple Variables selected.
            * For each variable:
                * There is 0 or 1 Value selected.
        3. There are multiple Series selected.
        4. For each series.
            * There is 1 Graph selected.
            * There is 1 Graph Style selected.
            * There is 1 Graph Axis selected.
        5. There are multiple Graphs.

    Given this, the State Storage should have a shape like this:
        [
            {
                'Operacion': op_id,
                'Tabla': tab_id,
                'VariableValor': [
                    {
                        'Variable': var_id,
                        'Valor': val_id
                    }
                ],
                'Serie': [
                    {
                        'Serie': serie_id,
                        'Graph': {
                            'Id': 'Graph_id',
                            'Axis': 'GraphAxis',
                            'Style': 'GraphStyle'
                        }
                    }
                ]
            }
        ]

    Para simplificar se puede reducir a lo siguiente:
        {
            op_id: {
                'Tabla': tab_id,
                'VariableValor': {
                    var_id: val_id
                },
                'Serie': {
                    serie_id: {
                        'GraphNumber': GraphNumber,
                        'Axis': GraphAxis,
                        'Style': GraphStyle
                    }
                }
            }
        }
    """


    """Iniciamos el servidor de dash."""
    app = Dash()

    app.layout = html.Div(
        children=[
            SESSION_STORAGE,
            STATE_STORAGE,
            SB.SelectionBoxComponent(1)
        ]
    )
    SB.event_listeners_adder(1)
    app.run(debug=True)
    return None


if __name__ == '__main__':
    main()
