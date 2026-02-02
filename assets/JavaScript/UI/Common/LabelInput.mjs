import dash from './dash_components.mjs';

function LabelInput(label, inputComp, style='top'){
    const span = dash._html.Span({'children': label});
    if (style === 'top'){
        return dash._html.Div({
            'children': [span, inputComp],
            'className': 'LabelInput LITop'
        });
    }
    else if (style === 'side'){
        return dash._html.Div({
            'children': [span, inputComp],
            'className': 'LabelInput LISide'
        });
    }
    else {
        throw new Error('style can only be side or top');
    }
    return null;
}

export default LabelInput;