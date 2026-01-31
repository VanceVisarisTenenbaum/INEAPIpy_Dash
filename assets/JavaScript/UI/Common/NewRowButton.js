
import dash from './dash_components.js';
import id_generator from './Functions/id_generators.js';

function NewRowButtonComp(name, row_lv1=null){

    const boton = dash._html.Button({
        'children': 'Nueva fila',
        'n_clicks': 0,
        'id': id_generator('Input', name, 'Button', row_lv1),
        'className': 'Button'
    })
    const comp = dash._html.Div({
        'children': [boton],
        'className': 'ButtonContainer'
    })
    return comp;
}

export default NewRowButtonComp;