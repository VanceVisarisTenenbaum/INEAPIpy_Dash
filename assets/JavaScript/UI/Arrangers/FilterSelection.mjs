import dash from '../Common/dash_components.mjs';
import id_generator from '../Common/Functions/id_generator.mjs';
import NewRowButtonComp from '../Common/NewRowButton.mjs';
import OperationComponent from '../Inputs/OperationComponent.mjs';
import TableComponent from '../Inputs/TableComponent.mjs';
import VVP from './VarValPairsBox.mjs';

function FiltersRow(row_lv1, op_comp, tab_comp, varvalbox_comp){
    const comp = dash._html.Div({
        'children': [
            op_comp,
            dash._html.Div({
                'children': [tab_comp, varvalbox_comp],
                'className': 'ColSplitterBase ColSplitterBig',
                'id': id_generator('Arranger', 'TablaVVP', null, row_lv1)
            })
        ],
        'id': id_generator('Arranger', 'FiltersRow', null, row_lv1)
    })

    return comp;
}

function InputSelectionBox(initial_IGR){
    const comp = dash._html.Div({
        'children': [
            _html.Div({
                'children': [initial_IGR],
                'className': 'filter-list',
                'id': id_generator('Arranger', 'FilterSelection')
            }),
            NewRowButtonComp('Filtro', null)
        ],
        'id': id_generator('Arranger', 'FilterSelection', 'Box')
    })
    return comp;
}


function make_FR(row_lv1){
    const OpC = OperationComponent(row_lv1);
    const TbC = TableComponent(row_lv1, null);
    const VVPBox = VVP.VarValPairBoxComponent(row_lv1,
                                              VVP.make_vvp(row_lv1, 1));
    const comp = FiltersRow(row_lv1, OpC, TbC, VVPBox);
    return comp;
}


export default {InputsGroupRow, InputSelectionBox, make_FR};