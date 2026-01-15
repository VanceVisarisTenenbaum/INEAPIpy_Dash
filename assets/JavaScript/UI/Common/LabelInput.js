import dash from './dash_components.js';

function LabelInput(label, inputComp, style='top'){
    if (style === 'top'){
        return dash._html.Div({
            'children': [dash._html.Span(label), inputComp],
            'className': 'LabelInput LITop'
        });
    }
    else if (style === 'side'){
        return dash._html.Div({
            'children': [dash._html.Span(label), inputComp],
            'className': 'LabelInput LISide'
        });
    }
    else {
        throw new Error('style can only be side or top');
    }
    return null;
}

export default LabelInput;