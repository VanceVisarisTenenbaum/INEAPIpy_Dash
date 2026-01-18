
function get_storage_content(storage_key, default_val=null){
    return JSON.parse(sessionStorage.getItem(storage_key)) || default_val;
}

function write_to_storage(storage_key, content){
    sessionStorage.setItem(storage_key, JSON.stringify(content));
    return null;
}

export default {get_storage_content, write_to_storage};