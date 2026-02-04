
function switch_f(n_clicks, current_state){
    if (current_state === 'light'){return 'dark';}
    else {return 'light';}
}


window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'light_dark_switch': {
            'switch_f': switch_f
        }
    }
);