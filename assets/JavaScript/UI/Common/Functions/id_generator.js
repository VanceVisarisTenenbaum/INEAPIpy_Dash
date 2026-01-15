

function id_generator(name, tipo=null, row_lv1=null, row_lv2=null){
    let = id_name = `type: ${name}`;
    if (tipo != null){id_name += `${tipo}`;}
    if (row_lv1 != null){
        let id_row1 = `fila_lv1: ${row_lv1}`;
        id_name += id_row1;
        if (row_lv2 != null){
            let id_row2 = `fila_lv2: ${row_lv2}`;
            id_name += id_row2;
        }
    }
    return id_name;
}

function name_mapper(short_name){
    map_dict = {
        'O': 'Operacion',
        'T': 'Tabla',
        'Vr': 'Variable',
        'Vl': 'Valor',
        'G': 'Grafica',
    }
    return map_dict[short_name] || short_name
}

function id_generator_mapper(name, tipo=null, row_lv1=null, row_lv2=null){
    return id_generator(name_mapper(name), tipo, row_lv1, row_lv2);
}


export default {id_generator_mapper, name_mapper};