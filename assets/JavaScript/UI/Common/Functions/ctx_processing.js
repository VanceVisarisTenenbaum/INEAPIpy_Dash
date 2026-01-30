

function get_trigerred_id(){
    return dash_clientside.callback_context.triggered_id;
}

function get_triggered_value(){
    return dash_clientside.callback_context.triggered[0]['value'];
}

function get_value_of_matching_id(list_of_)