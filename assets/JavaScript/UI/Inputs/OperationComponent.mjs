import SelectComponent from '../Common/SelectComponent.mjs';
import get_from_requests_storage from '../../Storage/RequestsStorage.mjs';

function OperationComponent(row_lv1){
    const operaciones = get_from_requests_storage('Operaciones');
    const comp = SelectComponent(operaciones, 'Operacion', row_lv1);
    return comp;
}

export default OperationComponent;