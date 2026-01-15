import idgen from './Functions/id_generator.js';
import extract_labels_values from './Functions/ine_processing.js';

function SelectComponent(list_of_ine_obj,
                         name,
                         fila_lv1, fila_lv2=null,
                         multi=False){
    let placeholder_v;
    if (multi){placeholder_v = 'Selecciona una o varias ' + name_mapper(name);}
    else {placeholder = 'Selecciona una '  + name_mapper(name);}

    let IC = _dcc.Dropdown({
        'options': extract_labels_values(list_of_ine_obj),
        'value': null,
        'id': idgen.id_generator_mapper(name, null, fila_lv1, fila_lv2),
        'className': 'Input Dropdown',
        'multi': multi,
        'placeholder': placeholder_v
    });
    return LabelInput(idgen.name_mapper(name), IC);
}


export default SelectComponent;