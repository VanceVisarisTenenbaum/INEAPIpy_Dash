
import RS from '../../Storage/RequestsStorage.js';

// This event listener is triggered when an input is selected in the client
// In case it is requested, the output is not updated
// If it is not, then updates the output, which trigers the request
// in the server.

function check_requested_val_maker(input_type){
    function check_requested_val(input_val, server_dummy_storage){
        /*
        Checks if the val was already requested.
        */
        const data = RS.get_from_requests_storage(input_type, input_val);
        if (data === null){return window.dash_clientside.no_update;}
        server_dummy_storage['last_update'] = Math.random() * 1000;
        return server_dummy_storage
    }
    return check_requested_val;
}


window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'input_check': {
            'check_requested_operation': check_requested_val_maker('Variable'),
            'check_requested_variable': check_requested_val_maker('Valor'),
        }
    }
);