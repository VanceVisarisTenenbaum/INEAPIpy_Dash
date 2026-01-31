


function add_update(name, dummy_storage){
    dummy_storage['last_update'] = name;
    return dummy_storage;
}

function get_last_update(dummy_storage){
    return dummy_storage['last_update'];
}


export default {add_update, get_last_update};