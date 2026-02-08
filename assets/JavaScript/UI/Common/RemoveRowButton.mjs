import dash from './dash_components.mjs';
import id_generator from './Functions/id_generator.mjs';


function RemoveRowButton(row_lv1, row_lv2='', is_pair=false){
    let class_name;
    let class_2;

    if (is_pair){
        class_name = 'cross';
        class_2 = 'btn-delete-pair';
    }
    else {
        class_name = 'trash-can';
        class_2 = 'btn-delete-card';
    }

    const comp = dash._html.Button({
        'children': dash._html.Div({'children': '', 'className': 'svg ' + class_name}),
        'className': 'btn-delete ' + class_2,
        'id': id_generator('Input', 'EliminarFila', 'Button', row_lv1, row_lv2)
    })

    return comp;
}

export default RemoveRowButton;