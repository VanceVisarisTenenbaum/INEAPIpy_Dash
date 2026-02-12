

function select_serie_switch(n_clicks, current_state){
    if (current_state === "0"){return "1";}
    return "0";
}

window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'select_serie': {
            'select_serie_switch': select_serie_switch
        }
    }
);