import dash from '../Common/dash_components.mjs';
import id_generator from '../Common/Functions/id_generator.mjs';
import SelectComponent from '../Common/SelectComponent.mjs';
import get_from_requests_storage from '../../Storage/RequestsStorage.mjs';



function ReloadDataButton(){
    const comp = dash._html.Button({
        'children': [
            dash._html.Div({'children': '', 'className': 'svg reload'}),
            dash._html.Span({'children': 'Recargar Series'})
        ],
        'className': 'btn-refresh-table',
        'id': id_generator('Input', 'Recargar Series', 'Button')
    });
    return comp;
}


function TableTitle(){
    const comp = dash._html.Div({
        'children': [
            dash._html.H3({'children': 'Series', 'className': 'table-title'}),
            ReloadDataButton()
        ],
        'className': 'table-title-header'
    });
    return comp;
}


function Cell(data){
    const comp = dash._html.Div({
        'children': data,
        'className': 'cell'
    })
    return comp;
}

function TableHeader(){
    const cols = [
        'Operación (COD)',
        'Serie',
        'Grafica',
        'Eje Grafica'
    ];
    const cells = cols.map(col => Cell(col));
    const comp = dash._html.Div({
        'children': cells,
        'className': 'table-row header-row'
    });
    return comp;
}

function SelectedCheck(serie_id, row_lv1){
    const comp = dash._html.Div({
        'children': '',
        'className': 'svg circle check-icon row-checkbox',
        'id': id_generator('Input', 'Serie', 'Checkbox', row_lv1),
        'data-checked': "0",
        'data-serie-id': serie_id
    });
    return comp;
}

function SelectGrafica(row_lv1){
    const options = [{'Id': 1}];
    const comp = SelectComponent(options, 'Grafica', row_lv1, '', false, true)
    return comp;
}

function SelectGraficaAxis(row_lv1){
    const options = [{'Id': 1}, {'Id': 2}];
    const comp = SelectComponent(options, 'Eje Grafica', row_lv1, '', false, true);
    return comp;
}


function get_operation_name(op_id){
    const OPs = get_from_requests_storage('Operaciones');
    for (const op of OPs){
        if (op['Id'] === op_id){
            return op['Nombre'];
        }
    }
    return op_id;
}

function serie_data_to_row(serie_data, row_lv1){
    const data = [
        get_operation_name(serie_data['FK_Operacion']),
        serie_data['Nombre'],
        SelectGrafica(row_lv1),
        SelectGraficaAxis(row_lv1),
    ];

    const cells = data.map(d => Cell(d));

    const row = dash._html.Div({
        'children': cells,
        'className': 'table-row data-row',
        'id': id_generator('Label', 'Serie', 'Row', row_lv1),
        'data-checked': "0",
        'data-serie-id': serie_data['Id']
    })
    return row;
}

function TableOptions(list_of_series){
    const childs = list_of_series.map((data, i) => serie_data_to_row(data, i + 1));
    return childs;
}

function TableContainer(list_of_series=[]){
    const comp = dash._html.Div({
        'children': [
            TableHeader(),
            ...TableOptions(list_of_series)
        ],
        'className': 'custom-table-container',
        'id': id_generator('Container', 'Table')
    })
    return comp;
}

export default {TableOptions, TableContainer, TableHeader};


































