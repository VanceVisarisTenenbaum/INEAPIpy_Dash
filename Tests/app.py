# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 17:20:43 2025

@author: mano
"""


from dash import Dash, html, dcc, clientside_callback, Input, ALL, State, ClientsideFunction, Output


js_f = """
function read_drop(val, state){
    console.log(val);
    console.log('---------------')
    console.log(dash_clientside.callback_context);
    console.log('---------------')
    console.log(state)
    console.log('---------------')
    console.log(dash_clientside.callback_context.states);
    console.log('---------------')
    const tuVariable = dash_clientside.callback_context.states;
    Object.entries(tuVariable).forEach(([key, value]) =>{
        console.log('KEY:', key);
        console.log(typeof key);
        console.log('VALUE:', value);
    })
}
"""

clientside_callback(
    ClientsideFunction(
        namespace='sidebar_toggle',
        function_name='toggle'
    ),
    Output('sidebar-toggle', 'data-checked'),
    Input('hamburger-btn-label', 'n_clicks'),
    State('sidebar-toggle', 'data-checked')
)

def main():
    """Starts the App."""


    """Iniciamos el servidor de dash."""
    app = Dash(__name__, assets_folder='../assets')

    app.layout = html.Div(
        children=[
            html.Div(
                children='',
                **{'id':'sidebar-toggle', 'data-checked':1}
            ),
            html.Div(
                children=[
                    html.Header( ####################################
                        children=[
                            html.Div(
                                children=[
                                    html.Label(
                                        children=[
                                            html.Div(className='hamburger-btn')
                                        ],
                                        htmlFor='sidebar-toggle',
                                        className='hamburger-btn-label',
                                        style={'display': 'inline'},
                                        **{'id':'hamburger-btn-label'}
                                    ),
                                    html.H1('Buscador INE', className='title')
                                ],
                                className='header-left'
                            ),
                            html.Div(
                                className='header-right'
                            )
                        ],
                        className='header'
                    ),
                    html.Label(htmlFor='sidebar-toggle',
                               className='mobile-backdrop',
                               style={'display': 'inline'}),

                    # Sidebar
                    html.Aside(
                        className='sidebar'
                    ),
                    # Main
                    html.Main(
                        className='main'
                    )
                ],
                className='main-layout'  # Lo que layout-grid por gemini
            )
        ]
    )
    app.run(debug=True)
    return None


if __name__ == '__main__':
    main()