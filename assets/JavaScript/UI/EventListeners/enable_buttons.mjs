

function enable_var_val_button(op_id_val){
    if (op_id_val === null || op_id_val === undefined){return true;}
    return false;
}

window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'enable_buttons': {
            'enable_var_val_button': enable_var_val_button,
        }
    }
);