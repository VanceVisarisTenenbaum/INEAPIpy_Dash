import get_from_requests_storage from '../../Storage/RequestsStorage.mjs';
import ctx from '../Common/Functions/ctx_processing.mjs';
import Logger from '../../Logger/logger.mjs';
import get from '../Common/Functions/dictionary_processing.mjs';

// This event listener is triggered when an input is selected in the client
// In case it is requested, the output is not updated
// If it is not, then updates the output, which trigers the request
// in the server.

const logger = new Logger();


function check_requested(input_){


    const id_ = ctx.get_triggered_id();

    if (id_ === null || id_ === undefined){
        return [ctx.no_update(), ctx.no_update()];
    }

    const input_type = get(id_, 'Nombre', null);
    const valor = ctx.get_triggered_value();

    logger.log(
        'Checking if value is already requested',
        ['Function', 'check_requested'],
        'Info',
        [id_, valor]
    );

    const input_output_map = {
        'Operacion': 'Variable',
        'Variable': 'Valor'
    }

    if (
        !Object.keys(input_output_map).includes(input_type)
        ||
        valor === null || valor === undefined
        ){
        return [ctx.no_update(), ctx.no_update()];
    }

    const data = get_from_requests_storage(input_output_map[input_type], valor);

    var patch = new dash_clientside.Patch;

    const out_ = {'Input Type': input_type, 'Valor': valor, 'Id': id_};
    const _patch = patch.assign(['last_update'], out_).build();
    if (data != null){
        return [ctx.no_update(), _patch];
    }
    return [_patch, ctx.no_update()];
}


window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'input_check': {
            'check_requested': check_requested,
        }
    }
);