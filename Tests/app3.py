# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 14:43:06 2026

@author: mano
"""

from dash import html, dcc, Input, Output, State, callback, clientside_callback, Dash


app = Dash(__name__)

app.layout = html.Div([
    dcc.Store('ServerTriggerer', storage_type='session', data={'Value': None}),
    dcc.Store('ClientTriggerer', storage_type='session', data={'Value': None}),
    html.Div(
        children=[
            dcc.Dropdown(
                options=['A', 'B', 'C'],
                **{'id': 'Select_That_Triggers'}  # I know I dont need the dict unpack, but id is a reserved function in python, so it bothers me to use it as key.
            ),
            dcc.Dropdown(
                options=[],
                **{'id': 'Select_That_Receives_Values'}
            )
        ]
    )
])


server_trigger_js = """
function trigger_server(val){
    console.log('Server triggerer called', val);
    var patch = new dash_clientside.Patch;
    const _patch = patch.assign(['Value'], val).build()
    if (val === null) {
        return [dash_clientside.no_update, _patch];
    }
    return [_patch, dash_clientside.no_update];
}
"""

client_update_dropdown_js = """
function update_dropdown(client_triggerer_data){
    console.log('Update Dropdown called');
    const options = client_triggerer_data['Value'];
    const patch = new dash_clientside.Patch;
    return patch.assign([], options).build();
}
"""


clientside_callback(
    server_trigger_js,
    Output('ServerTriggerer', 'data'),
    Output('ClientTriggerer', 'data', allow_duplicate=True),
    Input('Select_That_Triggers', 'value'),
    #State('ServerTriggerer', 'data'),
    #State('ClientTriggerer', 'data'),
    prevent_initial_call=True
)


@callback(
    Output('ClientTriggerer', 'data'),
    Input('ServerTriggerer', 'data'),
    State('ClientTriggerer', 'data'),
    prevent_initial_call=True
)
def get_options_server(server_triggerer_data, client_triggerer_data):
    print('server called')
    OPTIONS_MAP = {'A': [1,2,3], 'B': [4,5,6], 'C': [7,8,9]}
    selected_value = server_triggerer_data['Value']
    options = OPTIONS_MAP[selected_value]
    client_triggerer_data['Value'] = options
    return client_triggerer_data


clientside_callback(
    client_update_dropdown_js,
    Output('Select_That_Receives_Values', 'options'),
    Input('ClientTriggerer', 'data'),
    prevent_initial_call=True
)

if __name__ == '__main__':
    app.run(debug=True)