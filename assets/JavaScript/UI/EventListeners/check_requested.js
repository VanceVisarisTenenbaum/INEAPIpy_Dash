import RS from '../../Storage/RequestsStorage.js';
import ctx from '../Common/Functions/ctx_processing.js';
import Logger from '../../Logger/logger.js';
import get from '../Common/Functions/dictionary_processing.js';

// This event listener is triggered when an input is selected in the client
// In case it is requested, the output is not updated
// If it is not, then updates the output, which trigers the request
// in the server.

const logger = Logger();


function check_requested(input_, server_dummy_storage, client_dummy_storage){
    const id_ = ctx.get_triggered_id();
    const input_type = get(id_, 'Nombre', null);
    const data = RS.get_from_requests_storage(input_type, input_val);
    const valor = ctx.get_triggered_value()
    logger.log(
        'Checking if value is already requested',
        ['Function', 'check_requested'],
        'Info',
        [id_, valor]
    );

    conts out_ = {'Input Type': input_type, 'Valor': valor, 'Id': id_};
    if (data === null){
        client_dummy_storage['last_update'] = out_;
        return ctx.no_update(), client_dummy_storage;
    }
    server_dummy_storage['last_update'] = out_;
    return server_dummy_storage, ctx.no_update();
}


window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'input_check': {
            'check_requested': check_requested,
        }
    }
);