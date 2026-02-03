import dash from '../Common/dash_components.mjs';
import id_generator from '../Common/Functions/id_generator.mjs';
import NewRowButtonComp from '../Common/NewRowButton.mjs';
import VariableComponent from '../Inputs/VariableComponent.mjs';
import ValorComponent from '../Inputs/ValorComponent.mjs';


function VarValPair(var_comp, val_comp, row_lv1, row_lv2){
    const Comp = dash._html.Div({
        'children':[var_comp, val_comp],
        'className': 'ColSplitterBase',
        'id': id_generator('Arranger', 'ParVariableValor', null, row_lv1, row_lv2)
    });
    return Comp;
}


function VarValPairBoxComponent(row_lv1, initial_vvp){
    const vvp = dash._html.Div({
        'children': [initial_vvp],
        'id': id_generator('Arranger','ParesVariableValor', null, row_lv1),
        'className': 'RowSplitterBase RowSplitterSmall'
    })
    const comp = dash._html.Div({
        'children': [vvp, NewRowButtonComp('ParesVariableValor', row_lv1)]
    })
    return comp;
}


function make_vvp(row_lv1, row_lv2, variables=null, valores=null){
    const VrC = VariableComponent(row_lv1, row_lv2, variables);
    const VlC = ValorComponent(row_lv1, row_lv2, valores);
    return VarValPair(VrC, VlC, row_lv1, row_lv2);
}

export default {VarValPair, VarValPairBoxComponent, make_vvp};