function replace_null(val){
    if (val === null || val === undefined){return '';}
    return val;
}

function id_generator(ui_type='', ui_name='', ui_subtype='', row_lv1='', row_lv2=''){
    const id_ = {
        "Fila Nivel 1": replace_null(row_lv1),
        "Fila Nivel 2": replace_null(row_lv2),
        "Nombre": replace_null(ui_name),
        "Subtipo": replace_null(ui_subtype),
        "Tipo": replace_null(ui_type)
    };

    return id_;
}


export default id_generator;