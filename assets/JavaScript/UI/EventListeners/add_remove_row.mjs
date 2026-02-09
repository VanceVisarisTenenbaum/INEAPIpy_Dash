
import add from './add_new_row.mjs';
import del from './remove_row.mjs';
import ctx from '../Common/Functions/ctx_processing.mjs';


function update_var_val_row(n_clicks_add, n_clicks_remove, op_id){
    const patch = new dash_clientside.Patch;

    const triggered_id = ctx.get_triggered_id();
    const triggered_id_name = triggered_id['Nombre'];

    if (triggered_id_name === 'ParesVariableValor'){
        // Add process
        const newVVP = add.add_new_var_val_row(op_id);
        return patch.append([], newVVP).build();
    }
    else if (triggered_id_name === 'EliminarPar'){
        // Remove process
        const matching_index = del.remove_var_val_row();
        return patch.delete([matching_index]).build();
    }

}

function update_filter_row(n_clicks_add, n_clicks_remove){
    var patch = new dash_clientside.Patch;
    const triggered_id = ctx.get_triggered_id();
    const triggered_id_name = triggered_id['Nombre'];

    if (triggered_id_name === 'Filtro'){
        // AddProcess
        const newIB = add.add_new_FR();
        return patch.append([], newIB).build();
    }
    else if (triggered_id_name === 'EliminarFiltro'){
        // Remove process
        const matching_index = del.remove_filter_row();
        return patch.delete([matching_index]).build();
    }
}

window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'add_remove_row': {
            'update_var_val_row': update_var_val_row,
            'update_filter_row': update_filter_row
        }
    }
);