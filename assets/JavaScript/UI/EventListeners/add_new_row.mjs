import Logger from '../../Logger/logger.mjs';
import get_from_requests_storage from '../../Storage/RequestsStorage.mjs';
import VVP from '../Arrangers/VarValPairsBox.mjs';
import IGB from '../Arrangers/InputsBox.mjs';
import id_generator from '../Common/Functions/id_generator.mjs';
import doc from '../Common/Functions/document_processing.mjs';
import ctx from '../Common/Functions/ctx_processing.mjs';


const logger = new Logger();

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

    const row_lv2 = current_children.length + 1;

    //const op_id = ctx.get_value_of_matching_state(['Fila Nivel 1']);

    const variables = get_from_requests_storage('Variable', op_id);
    const newVVP = VVP.make_vvp(row_lv1, row_lv2 + 1, variables, null);

    return patch.append([], newVVP).build();
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
    const current_children = doc.get_element_by_id(ISB_ID);
    const row_lv1 = current_children.children.length + 1;
    const newIB = IGB.make_IGR(row_lv1);
    return patch.append([], newIB).build();
}

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
        'InputSelection': IGB.make_IGR(row_lv1_ISB),
        //'ParesVariableValor': VVP.make_vvp(row_lv1_VVP, row_lv1_ISB)
    };
    return patch.append([], name_new_row_map[button_id['Nombre']]).build();
}

window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'add_row': {
            'add_new_var_val': add_new_var_val_row,
            'add_new_IB': add_new_IB
        }
    }
);