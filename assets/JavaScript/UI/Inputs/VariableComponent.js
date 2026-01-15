import SelectComponent from '../Common/SelectComponent.js';

function VariableComponent(row_lv1, row_lv2, list_of_ine_var){
    return SelectComponent(list_of_ine_var, 'Vr', row_lv1, row_lv2);
}