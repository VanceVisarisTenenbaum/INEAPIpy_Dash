import SP from '../UI/Common/Functions/storage_processing.mjs';
import get from '../UI/Common/Functions/dictionary_processing.mjs';
import Logger from '../Logger/logger.mjs';
import id_generator from '../UI/Common/Functions/id_generator.mjs';

const logger = new Logger();
function get_from_requests_storage(obj_type, obj_depend=null){
    logger.log('Requested data from requests storage',
               ['Fuction', 'get_from_requests_storage'],
               'Info',
               [obj_type, obj_depend]);

    const storage_id = JSON.stringify(id_generator('Storage', 'Requests'));
    const requests_storage = SP.get_storage_content(storage_id);
    const precomputed_types = ['Operaciones', 'Publicaciones', 'Unidades',
                               'Escalas', 'Periodicidades'];
    if (precomputed_types.includes(obj_type)){
        return get(requests_storage, obj_type);
    }

    if (!Number.isInteger(obj_depend)){
        logger.log('obj_depend must be a an integer',
                   ['Fuction', 'get_from_requests_storage'],
                   'Error',
                   ['Your input:', obj_depend]);
        throw new Error('obj_depend must be an integer.');
    }
    const valid_types = ['Variable', 'Valor', 'Tabla', 'Periodo', 'Serie', 'Data']
    if (!valid_types.includes(obj_type)){
        logger.log('obj_type must be a valid value',
                   ['Fuction', 'get_from_requests_storage'],
                   'Error',
                   ['Your input:', obj_type,
                    'Valid options:', valid_types]);
        throw new Error('obj_type must be a valid value');
    }

    const data = get(get(requests_storage, obj_type), obj_depend, null);
    if (data === null){
        logger.log('Data not found',
                   ['Fuction', 'get_from_requests_storage'],
                   'Warning',
                   ['Your input:', [obj_type, obj_depend]]);
    }
    return data;
}

export default get_from_requests_storage;