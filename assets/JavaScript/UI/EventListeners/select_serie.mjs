import id_generator from '../Common/Functions/id_generator.mjs';
import SP from '../Common/Functions/storage_processing.mjs';


function pop(lista, val){
    return lista.filter(el => el != val);
}


function select_serie_switch(n_clicks, current_state, serie_val){
    const storage_id = JSON.stringify(id_generator('Storage', 'Dummy', 'Selected_Series'));
    let storage = SP.get_storage_content(storage_id);
    if (storage['last_update'] === -1){storage = [];}

    if (current_state === "0"){
        storage.push(serie_val);
        SP.write_to_storage(storage_id, storage);
        return "1";
    }
    const new_list = pop(storage, serie_val);
    SP.write_to_storage(storage_id, new_list);
    return "0";
}

window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'select_serie': {
            'select_serie_switch': select_serie_switch
        }
    }
);