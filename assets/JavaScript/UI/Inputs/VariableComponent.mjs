import SelectComponent from '../Common/SelectComponent.mjs';

function VariableComponent(row_lv1, row_lv2, list_of_ine_var){
    return SelectComponent(list_of_ine_var, 'Variable', row_lv1, row_lv2);
}

export default VariableComponent;