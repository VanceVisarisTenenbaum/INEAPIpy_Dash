import ctx from '../Common/Functions/ctx_processing.mjs';
import ss from '../../Storage/StateStorage.mjs';
import Logger from '../../Logger/logger.mjs';
import get from '../Common/Functions/dictionary_processing.mjs';


const logger = new Logger();
function store_selected(input_, state_storage, series_){
    // Input is any dropdown
    // series is all serie drowdowns
    const id_ = ctx.get_triggered_id();
    if (id_ === null || id_ === undefined){return ctx.no_update();}


    const row_lv1 = get(id_, 'Fila Nivel 1', null);
    const row_lv2 = get(id_, 'Fila Nivel 2', null);
    const input_val = ctx.get_triggered_value();
    const input_type = get(id_, 'Nombre', null);

    // We check if the trigger was adding or removing a row.
    if (input_val === ss.get_current_value(row_lv1, row_lv2,
                                           input_type, state_storage)){
        return ctx.no_update();
    }

    logger.log(
        'Storing selected input',
        ['Function', 'store_selected'],
        'Info',
        [id_, input_val]
    );

    const patch_ = new dash_clientside.Patch;
    if (['Variable', 'Valor'].includes(input_type)){
        const val = ss.update_selected(input_type)(row_lv1, row_lv2,
                                           null, input_val,
                                           state_storage);
        const _patch = patch_.assign([], val).build();
        return _patch
    }
    else if (['Graph', 'Graph Axis', 'Graph Style'].includes(input_type)){
        return ctx.no_update();
        //let serie_id = ctx.get_value_of_matching_state(['Fila Nivel 1']);
        /*
        return ss.update_selected(input_type)(row_lv1, serie_id,
                                           null, input_val,
                                           state_storage);*/
    }
    else {
        const val = ss.update_selected(input_type)(row_lv1,
                                           null, input_val,
                                           state_storage);
        const _patch = patch_.assign([], val).build();
        return _patch;
    }
}

/* ------------------------------------------------------------------------- */

window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'state_storage': {
            'store_selected': store_selected
        }
    }
);