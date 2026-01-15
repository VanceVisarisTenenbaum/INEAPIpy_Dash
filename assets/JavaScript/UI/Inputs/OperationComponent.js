import SelectComponent from '../Common/SelectComponent.js';

function OperationComponent(row_lv1, requests_storage){
    const operaciones = requests_storage['Operaciones'];
    const comp = SelectComponent(operaciones, 'O', row_lv1);
    return comp;
}

export default OperationComponent;