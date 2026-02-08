import Logger from '../../Logger/logger.mjs';
import get_from_requests_storage from '../../Storage/RequestsStorage.mjs';
import VVP from '../Arrangers/VarValPairsBox.mjs';
import FS from '../Arrangers/FilterSelection.mjs';
import id_generator from '../Common/Functions/id_generator.mjs';
import doc from '../Common/Functions/document_processing.mjs';
import ctx from '../Common/Functions/ctx_processing.mjs';


const logger = new Logger();


function get_id_key(children, key){
    const id_str = children.id;
    return JSON.parse(id_str)[key];
}

function get_max_key(childrens_list, key){
    return Math.max(...Array.from(childrens_list, el => get_id_key(el, key)))
}

function add_new_var_val_row(n_clicks, op_id){
    logger.log(
        'Add new Variable Value Pair Row, function called',
        ['Function', 'add_new_var_val_row'],
        'Info',
        [n_clicks, op_id]
    )
    const patch = new dash_clientside.Patch;
    const triggered_id = ctx.get_triggered_id();

    const row_lv1 = triggered_id['Fila Nivel 1'];
    const VVPB_id = id_generator('Arranger', 'ParesVariableValor', null, row_lv1);

    const current_children = doc.get_element_by_id(VVPB_id).children;

    const last_row = get_max_key(current_children, 'Fila Nivel 2');
    const row_lv2 = last_row + 1;

    //const op_id = ctx.get_value_of_matching_state(['Fila Nivel 1']);

    const variables = get_from_requests_storage('Variable', op_id);
    const newVVP = VVP.make_vvp(row_lv1, row_lv2, variables, null);

    return patch.append([], newVVP).build();
}

function add_new_FR(n_clicks){
    logger.log(
        'Add new Inputs Row, function called',
        ['Function', 'add_new_FR'],
        'Info',
        [n_clicks]
    )
    const patch = new dash_clientside.Patch;
    const FR_ID = id_generator('Arranger', 'FilterSelection');
    const current_children = doc.get_element_by_id(FR_ID).children;
    const last_row = get_max_key(current_children, 'Fila Nivel 1');
    const row_lv1 = last_row + 1;
    const newIB = FS.make_FR(row_lv1);
    return patch.append([], newIB).build();
}
/*
function add_new_row_process(n_clicks){
    const patch = new dash_clientside.Patch;
    const button_id = ctx.get_triggered_id();
    const parent_id = id_generator('Arranger',
                                   button_id['Nombre'],
                                   null,
                                   button_id['Fila Nivel 1'],
                                   button_id['Fila Nivel 2']
                                   )
    const current_children = doc.get_element_by_id(parent_id).children;
    const row_lv1_ISB = current_children.length + 1;
    const row_lv1_VVP = button_id['Fila Nivel 1'];
    const name_new_row_map = {
        'InputSelection': FS.make_FR(row_lv1_ISB),
        //'ParesVariableValor': VVP.make_vvp(row_lv1_VVP, row_lv1_ISB)
    };
    return patch.append([], name_new_row_map[button_id['Nombre']]).build();
}
*/
window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'add_row': {
            'add_new_var_val': add_new_var_val_row,
            'add_new_FR': add_new_FR
        }
    }
);