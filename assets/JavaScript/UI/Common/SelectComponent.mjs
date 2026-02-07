import id_generator from './Functions/id_generator.mjs';
import extract_labels_values from './Functions/ine_processing.mjs';
import dash from './dash_components.mjs';
import LabelInput from './LabelInput.mjs';

function SelectComponent(list_of_ine_obj,
                         name,
                         fila_lv1, fila_lv2='',
                         multi=false){


    let list_of_labels_values;
    if (list_of_ine_obj === null){list_of_labels_values = [];}
    else {list_of_labels_values = extract_labels_values(list_of_ine_obj)}



    const summary = dash._html.Summary({
        'children': [
            dash._html.H3({'children': name}),
            dash._html.Span({'children': '', 'className': 'svg chevron-down'})
        ],
        'className': 'collapse-header'
    })

    const selection = dash._dcc.RadioItems({
        'options': list_of_labels_values,
        'className': 'radio-custom',
        'value': null,
        'id': id_generator('Input', name, 'Dropdown', fila_lv1, fila_lv2)
    })

    const component = dash._html.Details({
        'children': [
            summary,
            selection
        ],
        'className': 'custom-collapse'
    })


    return component;
}


export default SelectComponent;