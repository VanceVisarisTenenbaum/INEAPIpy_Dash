# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 17:20:43 2025

@author: mano
"""


from dash import Dash, html, dcc, clientside_callback, Input, ALL, State


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



def main():
    """Starts the App."""


    """Iniciamos el servidor de dash."""
    app = Dash()

    app.layout = html.Div(
        children=[
            dcc.Checklist(
                options=[
                    {'label': '', 'value': 'Checked'}
                ],
                value='Checked',
                **{'id': 'sidebar-toggle'}
            ),
            html.Div(
                children=[
                    html.Header( ####################################
                        children=[
                            html.Div(
                                children=[
                                    html.Label(
                                        htmlFor='sidebar-toggle',
                                        className='hamburger-btn'
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
                               className='mobile-backdrop'),

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
    print(app.layout.to_plotly_json())
    app.run(debug=True)
    return None


if __name__ == '__main__':
    main()