import extract_labels_values from '../Common/Functions/ine_processing.mjs';
import get_from_requests_storage from '../../Storage/RequestsStorage.mjs';
import ctx from '../Common/Functions/ctx_processing.mjs';
import id_generator from '../Common/Functions/id_generator.mjs';

function get_valid_options(obj_type, obj_depend){
    const data = get_from_requests_storage(obj_type, obj_depend);
    const options = extract_labels_values(data);
    return options;
}


function add_options_to_input(client_dummy_storage){

    const input_output_map = {
        'Operacion': ['Variable', 'Tabla'],
        'Variable': ['Valor']
    }

    const input_ = client_dummy_storage['last_update']
    const id_ = input_['Id']

    let output_id;
    let row_lv2;
    let options;
    if (input_['Input Type'] === 'Operacion'){row_lv2 = 1;}
    else {row_lv2 = input_['Input Type'];}
    for (let output_type of input_output_map[input_['Input Type']]){

        output_id = id_generator(
            'Input', output_type, 'Dropdown',
            input_['Fila Nivel 1'],
            row_lv2
        )
        options = get_valid_options(output_type, input_['Valor']);
        dash_clientside.set_props(output_id, {'options': options});
    }

    return null;
}


window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'add_options_to_inputs': {
            'add_options_to_input': add_options_to_input,
        }
    }
);