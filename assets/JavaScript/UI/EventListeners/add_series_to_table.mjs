import STS from '../Arrangers/SeriesTableSelector.mjs';
import SP from '../Common/Functions/storage_processing.mjs';
import id_generator from '../Common/Functions/id_generator.mjs';

function add_series(series_dummy_storage_data){
    const patch = new dash_clientside.Patch;
    const series_rows = STS.TableOptions(series_dummy_storage_data);
    const childrens = [STS.TableHeader(), ...series_rows];
    const patch_ = patch.assign([], childrens).build();
    // Once series has been reloaded, we delete the requested series storage_processing
    const storage_id = JSON.stringify(id_generator('Storage', 'Dummy', 'Selected_Series'));
    SP.write_to_storage(storage_id, []);
    return patch_;
}


window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'add_series_to_table': {
            'add_series': add_series
        }
    }
);
