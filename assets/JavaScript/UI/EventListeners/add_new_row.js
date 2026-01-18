import Logger from '../../Logger/logger.js';
import get_from_requests_storage from '../../Storage/RequestsStorage.js';
import VVP from '../Arrangers/VarValPairsBox.js';
import IGB from '../Arrangers/InputsBox.js';
import idgen from '../Common/Functions/id_generator.js';
import doc from '../Common/Functions/document_processing.js';


const logger = Logger();

function add_new_var_val_row(n_clicks, op_id){
    logger.log(
        'Add new Variable Value Pair Row, function called',
        ['Function', 'add_new_var_val_row'],
        'Info',
        [n_clicks, op_id]
    )
    const patch = new dash_clientside.Patch;
    const triggered_id = dash_clientside.callback_context.triggered_id

    const current_children = doc.get_element_by_id(triggered_id).children;
    const row_lv1 = triggered_id['fila_lv1'];
    const row_lv2 = current_children.length + 1;

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
    const current_children = doc.get_element_by_id('ISB');

    const row_lv1 = current_children.length + 1;
    const newIB = IGB.make_IGR(row_lv1);
    patch.append(newIB);
    return patch;
}


window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'add_row': {
            'add_new_var_val_row': add_new_var_val_row,
            'add_new_op_row': add_new_IB,
        }
    }
);