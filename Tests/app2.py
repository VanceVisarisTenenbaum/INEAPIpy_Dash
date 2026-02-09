# Set shebang if needed
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 10:11:23 2026

@author: mano
"""

# app.py
from dash import Dash, html, dcc, Input, Output, callback, no_update
import time

app = Dash(__name__)

app.layout = html.Div([
    html.H3("Session Storage Debug - Minimal Example"),
    html.Button("Save All Stores", id="btn-save", n_clicks=0),
    html.Br(), html.Br(),

    html.Div([
        dcc.Store(id='store-1', storage_type='session', data={'counter': 0, 'name': 'first'}),
        dcc.Store(id='store-2', storage_type='session', data={'counter': 0, 'name': 'second'}),
        dcc.Store(id='store-3', storage_type='session', data={'counter': 0, 'name': 'third'}),
        dcc.Store(id='store-4', storage_type='session', data={'counter': 0, 'name': 'fourth'}),
        dcc.Store(id='store-5', storage_type='session', data={'counter': 0, 'name': 'fifth'}),
    ], style={'display': 'none'}),

    html.Div(id='output'),
    html.Pre(id='raw-session-storage'),
    dcc.Interval(id='interval', interval=1500, n_intervals=0)
])


# Simple callback that increments counters in ALL stores
@callback(
    Output('store-1', 'data'),
    Output('store-2', 'data'),
    Output('store-3', 'data'),
    Output('store-4', 'data'),
    Output('store-5', 'data'),
    Input('btn-save', 'n_clicks'),
    prevent_initial_call=True
)
def update_all_stores(n):
    if n is None:
        raise no_update

    new_data = {
        'counter': n,
        'name': f"updated-{n}",
        'timestamp': time.time()
    }

    return [new_data] * 5


# Just shows which stores Dash actually sees
@callback(
    Output('output', 'children'),
    Input('store-1', 'data'),
    Input('store-2', 'data'),
    Input('store-3', 'data'),
    Input('store-4', 'data'),
    Input('store-5', 'data'),
)
def show_what_dash_sees(s1, s2, s3, s4, s5):
    stores = [s1, s2, s3, s4, s5]
    lines = []
    for i, s in enumerate(stores, 1):
        if s is None:
            lines.append(f"Store {i}:  None / not loaded")
        else:
            lines.append(f"Store {i}:  counter = {s.get('counter')}, name = {s.get('name')}")
    return html.Ul([html.Li(line) for line in lines])


# Shows raw sessionStorage content (what the browser really has)
@callback(
    Output('raw-session-storage', 'children'),
    Input('interval', 'n_intervals')
)
def show_raw_session_storage(_):
    return (
        "Open developer tools (F12) → Application → Session Storage\n"
        "Look at key names that start with 'dcc:' or your component ids\n\n"
        "Also run in console:\n"
        "Object.keys(sessionStorage).filter(k => k.includes('store-'))"
    )


if __name__ == '__main__':
    app.run(debug=True)