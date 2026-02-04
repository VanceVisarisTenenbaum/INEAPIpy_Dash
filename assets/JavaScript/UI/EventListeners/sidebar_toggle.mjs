

function toggle(n_clicks, current_data_val){
    if (current_data_val === 1){return 0;}
    else {return 1;}
}

window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'sidebar_toggle': {
            'toggle': toggle
        }
    }
);