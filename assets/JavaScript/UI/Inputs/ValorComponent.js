import SelectComponent from '../Common/SelectComponent.js';

function ValorComponent(row_lv1, row_lv2, list_of_ine_val){
    return SelectComponent(list_of_ine_val, 'Vl', row_lv1, row_lv2);
}

export default ValorComponent;