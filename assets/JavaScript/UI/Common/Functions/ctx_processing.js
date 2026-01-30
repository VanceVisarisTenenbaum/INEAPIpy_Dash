

function get_trigerred_id(){
    return dash_clientside.callback_context.triggered_id;
}

function get_triggered_value(){
    return dash_clientside.callback_context.triggered[0]['value'];
}

function get_states(){
    return Object.entries(dash_clientside.callback_context.states);
}


function check_matching_property(obj1, obj2, prop){
    return obj1[prop] === obj2[prop];
}

function check_matching_properties(obj1, obj2, matching_properties){
    let cond = True;
    for (prop of matching_properties){
        cond = cond && check_matching_property(obj1, obj2, prop);
        // If at least one is False it will return false
    }
    return cond;
}


function get_value_of_matching_state(matching_properties){
    const id_ = get_trigerred_id();
    const states = get_states();
    let state_id;
    for (const [key, value] of states){
        state_id = JSON.parse(key.split('.')[0]);
        if (check_matching_properties(id_, state_id, matching_properties)){
            return value;
        };
    }
    return null;
}


export default {get_trigerred_id, get_triggered_value, get_states, get_value_of_matching_state};