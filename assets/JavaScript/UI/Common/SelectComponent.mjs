import id_generator from './Functions/id_generator.mjs';
import extract_labels_values from './Functions/ine_processing.mjs';
import dash from './dash_components.mjs';
import LabelInput from './LabelInput.mjs';

function SelectComponent(list_of_ine_obj,
                         name,
                         fila_lv1, fila_lv2='',
                         multi=false){

    if (list_of_ine_obj === null){list_of_ine_obj = [];}

    let placeholder_v;
    if (multi){placeholder_v = 'Selecciona una o varias ' + name;}
    else {placeholder_v = 'Selecciona una '  + name;}

    let IC = dash._dcc.Dropdown({
        'options': extract_labels_values(list_of_ine_obj),
        'value': null,
        'id': id_generator('Input', name, 'Dropdown', fila_lv1, fila_lv2),
        'className': 'Input Dropdown',
        'multi': multi,
        'placeholder': placeholder_v
    });
    return LabelInput(name, IC);
}


export default SelectComponent;