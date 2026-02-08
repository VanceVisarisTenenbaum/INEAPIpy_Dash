import Logger from '../../Logger/logger.mjs';
import id_generator from '../Common/Functions/id_generator.mjs';
import doc from '../Common/Functions/document_processing.mjs';
import ctx from '../Common/Functions/ctx_processing.mjs';


const logger = new Logger();

function get_matching_row_index(childrens_list, match_row_lv1, match_row_lv2=null){

    let id_str;
    let children;
    let id_;
    for (let index = 0; index < childrens_list.length; index++){
        children = childrens_list[index];
        id_ = JSON.parse(children.id);
        if (match_row_lv2 === null){
            if (id_['Fila Nivel 1'] === match_row_lv1){return index;}
        }
        else {
            if (
                id_['Fila Nivel 1'] === match_row_lv1
                &&
                id_['Fila Nivel 2'] === match_row_lv2
                ){return index;}
        }
    }
    throw new Error("Children not found.");
}


function remove_var_val_row(){

    const triggered_id = ctx.get_triggered_id();

    logger.log(
        'Removing Var Val Pair',
        ['Function', 'remove_var_val_row'],
        'Info',
        [triggered_id]
    )

    const row_lv1 = triggered_id['Fila Nivel 1'];
    const row_lv2 = triggered_id['Fila Nivel 2'];

    const VVPB_id = id_generator('Arranger', 'ParesVariableValor', null, row_lv1);

    const current_children = doc.get_element_by_id(VVPB_id).children;

    const matching_index = get_matching_row_index(current_children, row_lv1, row_lv2);

    return matching_index;
}

function remove_filter_row(){


    const triggered_id = ctx.get_triggered_id();

    logger.log(
        'Removing Filter',
        ['Function', 'remove_filter_row'],
        'Info',
        [triggered_id]
    )

    const row_lv1 = triggered_id['Fila Nivel 1'];

    const FR_ID = id_generator('Arranger', 'FilterSelection');
    const current_children = doc.get_element_by_id(FR_ID).children;

    const matching_index = get_matching_row_index(current_children, row_lv1);

    return matching_index;
}


export default {remove_var_val_row, remove_filter_row};

/*
window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'remove_row': {
            'remove_var_val_row': remove_var_val_row,
            'remove_filter_row': remove_filter_row
        }
    }
);
*/