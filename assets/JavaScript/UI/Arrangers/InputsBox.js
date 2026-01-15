import dash from '../Common/dash_components.js';
import idgen from '../Common/Functions/id_generator.js';
import NewRowButtonComp from '../Common/NewRowButton.js';

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

export default {InputsGroupRow, InputSelectionBox};