

function add_selected_operation(row_lv1, op_id, state_storage){

    state_storage[row_lv1] = {
        'Operacion': op_id,
        'Tabla': null,
        'VariableValor': {},
        'Serie': {}
    };
    return state_storage;
}

function update_selected_operation(row_lv1,
                                    prev_op_id, current_op_id,
                                    state_storage){
    return add_selected_operation(row_lv1, current_op_id, state_storage);
}


/* ------------------------------------------------------------------------- */
function add_selected_table(row_lv1, tab_id, state_storage){
    state_storage[row_lv1]['Tabla'] = tab_id;
    return state_storage;
}

function update_selected_table(row_lv1,
                                 prev_tab_id, current_tab_id, state_storage){
    return add_selected_table(row_lv1, current_tab_id, state_storage);
}


/* ------------------------------------------------------------------------- */
function add_selected_variable(row_lv1, row_lv2, var_id, state_storage){
    state_storage[row_lv1]['VariableValor'][row_lv2] = {
        'Variable': var_id,
        'Valor': null
    };
    return state_storage;
}

function update_selected_variable(row_lv1, row_lv2,
                                    prev_var_id, curr_var_id,
                                    state_storage){
    return add_selected_variable(row_lv1, row_lv2, curr_var_id, state_storage);
}


/* ------------------------------------------------------------------------- */
function add_selected_value(row_lv1, row_lv2, val_id, state_storage){
    state_storage[row_lv1]['VariableValor'][row_lv2]['Valor'] = val_id
    return state_storage;
}

function update_selected_value(row_lv1, row_lv2,
                                prev_val_id, curr_val_id,
                                state_storage){
    return add_selected_value(row_lv1, row_lv2, curr_val_id, state_storage);
}


/* ------------------------------------------------------------------------- */

function add_selected_serie(row_lv1, serie_id, state_storage){
    state_storage[row_lv1]['Serie'][serie_id] = {
        'Grafica': null,
        'Axis': null,
        'Style': null
    };
    return state_storage;
}

function pop(obj, key, defaultValue = null) {
  if (key in obj) {
    const value = obj[key];
    delete obj[key];
    return value;
  }
  return defaultValue;
}s

function update_selected_serie(row_lv1,
                                prev_serie_id, curr_serie_id,
                                state_storage){
    pop(state_storage[row_lv1]['Serie'], prev_serie_id, null);
    return add_selected_serie(row_lv1, curr_serie_id, state_storage);
}


/* ------------------------------------------------------------------------- */

function add_selected_graph(row_lv1, serie_id, graph_id, state_storage){
    state_storage[row_lv1]['Serie'][serie_id]['Grafica'] = graph_id;
    return state_storage;
}

function update_selected_graph(row_lv1, serie_id,
                                prev_graph_id, curr_graph_id,
                                state_storage){
    return add_selected_graph(row_lv1, serie_id, curr_graph_id, state_storage);
}


/* ------------------------------------------------------------------------- */

function add_selected_graph_style(row_lv1, serie_id, graph_style, state_storage){
    state_storage[row_lv1]['Serie'][serie_id]['Style'] = graph_style;
    return state_storage;
}

function update_selected_graph_style(row_lv1, serie_id,
                                    prev_graph_style, curr_grahp_style,
                                    state_storage){
    return add_selected_graph_style(row_lv1, serie_id, curr_grahp_style, state_storage);
}


/* ------------------------------------------------------------------------- */

function add_selected_graph_axis(row_lv1, serie_id, graph_axis, state_storage){
    state_storage[row_lv1]['Serie'][serie_id]['Axis'] = graph_axis;
    return state_storage;
}

function update_selected_graph_axis(row_lv1, serie_id,
                                    prev_graph_axis, curr_grahp_axis,
                                    state_storage){
    return add_selected_graph_axis(row_lv1, serie_id, curr_graph_axis, state_storage);
}


/* ------------------------------------------------------------------------- */

function get(obj, key, defaultValue = null) {
  return obj.hasOwnProperty(key) ? obj[key] : defaultValue;
}


function get_current_value(row_lv1, row_lv2, name, state_storage){
    const lv1 = get(state_storage, row_lv1, null);
    if (lv1 === null){return null;}

    if (['Operacion', 'Tabla'].includes(name)){return get(lv1, name);}
    else if (['Variable', 'Valor'.includes(name)]){
        const lv2 = get(get(lv1, 'VariableValor'), row_lv2, null);
        if (row_lv2 === null){return null;}
        return get(lv2, name);
    }
    else if (name === 'Serie'){return get(lv1, 'Serie');}
    else {throw new Error(
            'name can only be {Operacion, Tabla, Variable, Valor, Serie}');}
    return null;
}


/* ------------------------------------------------------------------------- */

function update_selected(input_type){
    const actions = {
        'Operacion': update_selected_operation,
        'Tabla': update_selected_table,
        'Variable': update_selected_variable,
        'Valor': update_selected_value,
        'Serie': update_selected_serie,
        'Graph': update_selected_graph,
        'Graph Axis': update_selected_graph_axis,
        'Graph Style': update_selected_graph_style,
    }

    return actions[input_type];
}

/* ------------------------------------------------------------------------- */

window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'state_storage': {
            'update_selected_operation': update_selected_operation,
            'update_selected_table': update_selected_table,
            'update_selected_variable': update_selected_variable,
            'update_selected_value': update_selected_value,
            'update_selected_serie': update_selected_serie,
            'update_selected_graph': update_selected_graph,
            'update_selected_graph_axis': update_selected_graph_axis,
            'update_selected_graph_style': update_selected_graph_style,
            'get_current_value': get_current_value
        }
    }
);



































