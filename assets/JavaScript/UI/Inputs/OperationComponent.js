import SelectComponent from '../Common/SelectComponent.js';
import get_from_requests_storage from '../../Storage/RequestsStorage.js';

function OperationComponent(row_lv1){
    const operaciones = get_from_requests_storage('Operaciones');
    const comp = SelectComponent(operaciones, 'O', row_lv1);
    return comp;
}

export default OperationComponent;