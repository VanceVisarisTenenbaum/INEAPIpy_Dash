import dash from '../Common/dash_components.js';
import idgen from '../Common/Functions/id_generator.js';
import NewRowButtonComp from '../Common/NewRowButton.js';
import VariableComponent from '../Inputs/VariableComponent.js';
import ValorComponent from '../Inputs/ValorComponent.js';


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


function make_vvp(row_lv1, row_lv2, variables=null, valores=null){
    const VrC = VariableComponent(row_lv1, row_lv2, variables);
    const VlC = ValorComponent(row_lv1, row_lv2, valores);
    return VarValPair(VrC, VlC, row_lv1, row_lv2);
}

export default {VarValPair, VarValPairBoxComponent, make_vvp};