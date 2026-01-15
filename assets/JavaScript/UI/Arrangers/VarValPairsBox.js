import dash from '../Common/dash_components.js';
import idgen from '../Common/Functions/id_generator.js';
import NewRowButtonComp from '../Common/NewRowButton.js';


function VarValPair(var_comp, val_comp, row_lv1, row_lv2){
    const Comp = dash._html.Div({
        'children':[var_comp, val_comp],
        'className': 'ColSplitterBase',
        'id': idgen.id_generator_mapper('VariableValor', None, row_lv1, row_lv2)
    });
    return Comp;
}


function VarValPairBoxComponent(row_lv1, initial_vvp){
    const vvp = dash._html.Div({
        'children': [initial_vvp],
        'id': idgen.id_generator_mapper('VariableValor', 'Box', row_lv1),
        'className': 'RowSplitterBase RowSplitterSmall'
    })
    const comp = dash._html.Div({
        'children': [vvp, NewRowButtonComp(row_lv1)]
    })
}

export default {VarValPair, VarValPairBoxComponent};