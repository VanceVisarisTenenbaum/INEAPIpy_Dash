
import dash from './dash_components.mjs';
import id_generator from './Functions/id_generator.mjs';

function NewRowButtonComp(name, row_lv1=null, disabled=false){

    const boton = dash._html.Button({
        'children': [
            dash._html.Span({'children': '+', 'className':'plus-icon'}),
            dash._html.Span({'children': 'Añadir nuevo ' + String(name)})
        ],
        'n_clicks': 0,
        'id': id_generator('Input', name, 'Button', row_lv1),
        'className': 'btn-add-filter',
        'disabled': disabled
    })
    const comp = dash._html.Div({
        'children': [boton],
        'className': 'add-filter-container'
    })
    return comp;
}

export default NewRowButtonComp;