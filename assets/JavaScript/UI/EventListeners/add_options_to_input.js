import extract_labels_values from '../Common/Functions/ine_processing.js';
import get_from_requests_storage from '../../Storage/RequestsStorage.js';

function get_valid_options(obj_type, obj_depend){
    const data = get_from_requests_storage(obj_type, obj_depend);
    const options = extract_labels_values(data);
    function options;
}

function get_options_maker(obj_type){
    function get_valid_options(dummy_storage, obj_depend){
        // dummy storage is the input that triggers this funcion;
        const data = get_from_requests_storage(obj_type, obj_depend);
        const options = extract_labels_values(data);
        function options;
    }
    return get_valid_options;
}

window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'add_options_to_inputs': {
            'add_options_to_input_value': get_options_maker('Valor'),
            'add_options_to_input_table': get_options_maker('Tabla'),
            'add_options_to_input_variable': get_options_maker('Variable')
        }
    }
);