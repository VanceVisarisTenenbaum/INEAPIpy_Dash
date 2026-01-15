


function extract_label_value(INE_object, onlyId = false) {
    if (typeof INE_object === 'object' && INE_object !== null) {
        if (onlyId) {
            return INE_object['Id'];
        }
        return { label: INE_object['Nombre'], value: INE_object['Id'] };
    } else {
        throw new Error('INE_object must be an object.');
    }
}

function extract_labels_values(listOfINE_Objects, onlyId = false) {
    if (Array.isArray(listOfINE_Objects)) {
        return listOfINE_Objects.map(x => extract_label_value(x, onlyId));
    } else if (typeof listOfINE_Objects === 'object' && listOfINE_Objects !== null) {
        return extract_label_value(listOfINE_Objects, onlyId);
    } else if (listOfINE_Objects === null){ return [];
    } else {
        throw new Error('list of INE object must be a list or object.');
    }
}


export default extract_labels_values;