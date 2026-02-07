import dash from '../Common/dash_components.mjs';
import id_generator from '../Common/Functions/id_generator.mjs';
import NewRowButtonComp from '../Common/NewRowButton.mjs';
import OperationComponent from '../Inputs/OperationComponent.mjs';
import TableComponent from '../Inputs/TableComponent.mjs';
import VVP from './VarValPairsBox.mjs';

function FiltersRow(row_lv1, op_comp, tab_comp, varvalbox_comp){


    const CardHeader = dash._html.Header({
        'children':[
            dash._html.Span({'children': 'Filtro ' + String(row_lv1)}),
            // Remove row button
        ],
        'className': 'card-header'
    })

    const OperationContainer = dash._html.Section({
        'children': [
            dash._html.Div({'children': 'Paso 1. Obligatorio.', 'className': 'step-label'}),
            op_comp
        ],
        'className':'logic-step logic-step-primary'
    })

    const TableWrapper = dash._html.Div({
        'children': tab_comp,
        'className': 'branch-col branch-a'
    })

    const VVPWrapper = dash._html.Div({
        'children': varvalbox_comp,
        'className': 'branch-col branch-b'
    })

    const TablaVariableValorGrid = dash._html.Div({
        'children': [
            TableWrapper,
            dash._html.Div({'children': '', 'className': 'or-divider-vertical'}),
            VVPWrapper
        ],
        'className': 'branches-grid',
        'id': id_generator('Arranger',
                           'TablaVVP',
                           null,
                           row_lv1)
    })

    const TableVariableValueWrapper = dash._html.Section({
        'children':[
            dash._html.Div({'children': 'Paso 2. Selecciona al menos una opción',
                            'className': 'branch-label'}),
            TablaVariableValorGrid
        ],
        'className': 'logic-branch-wrapper'
    })

    const FiltersWrapper = dash._html.Section({
        'children': [
            OperationContainer,
            dash._html.Div({'children': '', 'className': 'svg top-down-arrow'}),
            TableVariableValueWrapper
        ],
        'className': 'logic-flow-wrapper',
        'id': id_generator('Arranger',
                           'FiltersRow',
                           null,
                           row_lv1)
    })

    const comp = dash._html.Div({
        'children': [
            CardHeader,
            FiltersWrapper
        ],
        'className': 'filters-card'
    })

    return comp;
}

function FilterSelectionBox(initial_IGR){
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


export default {FiltersRow, FilterSelectionBox, make_FR};