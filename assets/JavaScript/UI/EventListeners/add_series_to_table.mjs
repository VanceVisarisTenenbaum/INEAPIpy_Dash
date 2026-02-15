import STS from '../Arrangers/SeriesTableSelector.mjs';

function add_series(series_dummy_storage_data){
    const patch = new dash_clientside.Patch;
    const series_rows = STS.TableOptions(series_dummy_storage_data);
    const childrens = [STS.TableHeader(), ...series_rows];
    console.log(series_rows, series_dummy_storage_data);
    const patch_ = patch.assign([], childrens).build();
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
