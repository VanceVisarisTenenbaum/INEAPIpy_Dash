import Logger from '../../Logger/logger.js';
import get_from_requests_storage from '../../Storage/RequestsStorage.js';
import VVP from '../Arrangers/VarValPairsBox.js';
import IGB from '../Arrangers/InputsBox.js';
import id_generator from '../Common/Functions/id_generator.js';
import doc from '../Common/Functions/document_processing.js';
import ctx from '../Common/Functions/ctx_processing.js';


const logger = Logger();

function add_new_var_val_row(n_clicks, op_){
    logger.log(
        'Add new Variable Value Pair Row, function called',
        ['Function', 'add_new_var_val_row'],
        'Info',
        [n_clicks, op_id]
    )
    const patch = new dash_clientside.Patch;
    const triggered_id = ctx.get_triggered_id();

    const current_children = doc.get_element_by_id(triggered_id).children;
    const row_lv1 = triggered_id['Fila Nivel 1'];
    const row_lv2 = current_children.length + 1;

    const op_id = ctx.get_value_of_matching_state(['Fila Nivel 1']);

    const variables = get_from_requests_storage('Variable', op_id);
    const newVVP = VVP.make_vvp(row_lv1, row_lv2 + 1, variables, null);
    patch.append(newVVP);
    return patch;
}

function add_new_IB(n_clicks){
    logger.log(
        'Add new Inputs Row, function called',
        ['Function', 'add_new_IB'],
        'Info',
        [n_clicks]
    )
    const patch = new dash_clientside.Patch;
    const ISB_ID = id_generator('Arranger', 'InputSelection');
    const current_children = doc.get_element_by_id(JSON.stringify(ISB_ID));

    const row_lv1 = current_children.length + 1;
    const newIB = IGB.make_IGR(row_lv1);
    patch.append(newIB);
    return patch;
}

function add_new_row_process(n_clicks){
    const patch = new dash_clientside.Patch;
    const button_id = ctx.get_triggered_id();
    const parent_id = id_generator(ui_type='Arranger',
                                   ui_name=button_id['Nombre'],
                                   ui_subtype=null,
                                   row_lv1=button_id['Fila Nivel 1'],
                                   row_lv2=button_id['Fila Nivel 2'],
                                   )
    const current_children = doc.get_element_by_id(JSON.stringify(parent_id));
    const row_lv1 = current_children.lenght + 1;
    const name_new_row_map = {
        'InputSelection': IGB.make_IGR(row_lv1),
    };
    patch.append(name_new_row_map[button_id['Nombre']]);
    return patch;
}

window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'add_row': {
            'add_new_row': add_new_row,
        }
    }
);