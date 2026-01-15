
import dash from './dash_components.js';
import idgen from './Functions/id_generators.js';

function NewRowButtonComp(row_lv1=null){
    let name;
    if (row_lv1 === null){name = 'O';}
    else {name = 'VariableValor'}
    const boton = dash._html.Button({
        'children': 'Nueva fila',
        'n_clicks': 0,
        'id': idgen.id_generator_mapper(name, 'Boton', row_lv1),
        'className': 'Button'
    })
    const comp = dash._html.Div({
        'children': [boton],
        'className': 'ButtonContainer'
    })
    return comp;
}

export default NewRowButtonComp;