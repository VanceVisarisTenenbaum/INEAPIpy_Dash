
function dashIdToDomId(idObj) {
    return String(JSON.stringify(idObj));
}

function get_element_by_id(id){
    const domID = dashIdToDomId(id);
    return document.getElementById(domID);
}

export default {get_element_by_id};