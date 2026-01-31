import SelectComponent from '../Common/SelectComponent.js';


function TableComponent(row_lv1, tab_options){
    return SelectComponent(tab_options, 'Tabla', row_lv1);
}


export default TableComponent;