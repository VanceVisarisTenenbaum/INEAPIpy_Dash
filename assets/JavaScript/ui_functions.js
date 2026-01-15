

// Custom components

function make_vvp(row_lv1, row_lv2){
    const VrC = VariableComponent(row_lv1, row_lv2, null);
    const VlC = ValorComponent(row_lv1, row_lv2, null);
    return VarValPair(VrC, VlC, row_lv1, row_lv2);
}

/* ------------------------------------------------------------------------- */



/* ------------------------------------------------------------------------- */

function get_from_requests_storage(obj_typ, obj_depend, requests_storage){
    if (Number.isInteger(obj_depend)){throw new Error('obj_depend must be an integer.');}
    if (!['Variable', 'Valor', 'Tabla', 'Periodo'].includes(obj_type)){
        throw new Error('obj_type must be a valid value');
    }
    const data = get(get(requests_storage, obj_type), obj_depend, null);
    if (data === null){throw new Error('Data not found')}
    return data;
}


function make_var_val_comp(op_id, row_lv1, row_lv2, requests_storage){

    const variables = get_from_requests_storage('Variable', op_id, requests_storage);
    const VrC = VariableComponent(row_lv1, row_lv2, variables);
    const VlC = ValorComponent(row_lv1, row_lv2, null);
    return VarValPair(VrC, VlC, row_lv1, row_lv2);
}

function add_new_var_val_row(n_clicks, current_childrens, op_id, requests_storage){
    const patch = new dash_clientside.Patch;

    const row_lv1 = dash_clientside.callback_context.triggered_id['fila_lv1'];
    const row_lv2 = current_childrens.length + 1;
    const newVVP = make_var_val_comp(op_id,
                                   row_lv1, row_lv2 + 1,
                                   requests_storage);
    patch.append(newVVP);
    return patch
}

function add_options_to_input_value(dummy_storage, var_id, requests_storage){
    // dummy is just the input trigger, must be unique to this function
    const valores = extract_labels_values(requests_storage['Valor'][var_id]);
    return valores;
}

function add_options_to_input_table(dummy_storage, op_id, requests_storage){
    // dummy is just the input trigger, must be unique to this function
    const tablas = extract_labels_values(requests_storage['Tabla'][op_id]);
    return tablas;
}

function add_options_to_input_variable(dummy_storage, op_id, requests_storage){
    // dummy is just the input trigger, must be unique to this function
    const variable = extract_labels_values(requests_storage['Variable'][op_id]);
    return variable;
}

function add_new_op_row(n_clicks, current_childrens, requests_storage){
    const patch = new dash_clientside.Patch;
    const row_lv1 = current_childrens.length + 1;
    const comp = InputsGroupRow(
        row_lv1,
        OperationSelectBox(row_lv1, requests_storage),
        TableSelectBox(row_lv1, []),
        VarValPairBoxComponent(
            row_lv1,
            make_vvp(row_lv1, 1)
        )
    );
    patch.append(comp);
    return patch;
}

/* ------------------------------------------------------------------------- */

window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'ui_functions': {
            'add_new_var_val_row': add_new_var_val_row,
            'add_options_to_input_value': add_options_to_input_value,
            'add_options_to_input_table': add_options_to_input_table,
            'add_options_to_input_variable': add_options_to_input_variable,
            'add_new_op_row': add_new_op_row
        }
    }
);
















