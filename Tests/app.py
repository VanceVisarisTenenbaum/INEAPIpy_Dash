# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 17:20:43 2025

@author: mano
"""


from dash import Dash, html, dcc, clientside_callback, Input


js_f = """
function read_drop(val){
    console.log(val);
    console.log('---------------')
    console.log(dash_clientside.callback_context.triggered_id);
}
"""

clientside_callback(js_f, Input({'Name': 'Drop', 'prop1': 2}, 'value'))


def main():
    """Starts the App."""


    """Iniciamos el servidor de dash."""
    app = Dash()

    app.layout = html.Div(
        children=[
            dcc.Dropdown(
                options=[1,2,3],
                className='B',
                **{'id': {'Name': 'Drop', 'prop1': 2}}
            )
        ],
        className='A'
    )
    print(app.layout.to_plotly_json())
    app.run(debug=True)
    return None


if __name__ == '__main__':
    main()