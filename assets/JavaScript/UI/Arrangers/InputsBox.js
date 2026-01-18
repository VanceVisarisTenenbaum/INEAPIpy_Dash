import dash from '../Common/dash_components.js';
import idgen from '../Common/Functions/id_generator.js';
import NewRowButtonComp from '../Common/NewRowButton.js';
import OperationComponent from '../Inputs/OperationComponent.js';
import TableComponent from '../Inputs/TableComponent.js';
import VVP from './VarValPairsBox.js';

function InputsGroupRow(row_lv1, op_comp, tab_comp, varvalbox_comp){
    const comp = dash._html.Div({
        'children': [
            op_comp,
            dash._html.Div({
                'children': [tab_comp, varvalbox_comp],
                'className': 'ColSplitterBase ColSplitterBig',
                'id': idgen.id_generator_mapper('TablaVVP', 'Box', row_lv1)
            })
        ],
        'id': idgen.id_generator_mapper('IG', None, row_lv1)
    })

    return comp;
}

function InputSelectionBox(initial_IGR){
    const comp = dash._html.Div({
        'children': [initial_IGR, NewRowButtonComp(null)],
        'className': 'RowSplitterBase RowSplitterBig',
        'id': 'ISB'
    })
    return comp;
}


function make_IGR(row_lv1){
    const OpC = OperationComponent(row_lv1);
    const TbC = TableComponent(row_lv1, null);
    const VVPBox = VVP.VarValPairBoxComponent(row_lv1,
                                              VVP.make_vvp(row_lv1, 1));
    const comp = InputsGroupRow(row_lv1, OpC, TbC, VVPBox);
    return comp;
}


export default {InputsGroupRow, InputSelectionBox, make_IGR};