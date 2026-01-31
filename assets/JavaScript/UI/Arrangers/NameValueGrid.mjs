import dash from '../Common/dash_components.mjs';


function dict_value_process(val){
  let newVal = '';

  if (Array.isArray(val)) {
      for (let i = 0; i < val.length; i++) {
          let v = val[i];
          let sep = (i % 3 === 0) ? '\n' : '; ';
          newVal += String(v) + sep;
      }
  } else if (typeof val === 'object' && !Array.isArray(val)) {
      throw new Error("val can't be a dict.");
  } else {
      newVal = String(val);
  }

  return newVal;
}


function NameValue(name_value_dict){
    childrens = [];
    Object.entries(name_value_dict).forEach(
        ([k,v]) => {
            let comp = dash._html.Div({
                'children': [
                    dash._html.Span(k, {'className': 'NameValName'}),
                    dash._html.Span(dict_value_process(v), {'className': 'NameValVal'})
                ],
                'className': 'NameValue'
            })
            childrens.push(comp);
        }
    );
    return dash._html.Div({
        'children': childrens,
        'className': 'NameValueGrid'
    });
}


function NameValueDisplayComponent(name_value_dict, comp_id, title=null){
    if (title === null){
        return dash._html.Div({
            'children': NameValue(name_value_dict),
            'id': comp_id
        })
    }
    else {
        return dash._html.Div({
            'children': [
                dash._html.H2(title),
                NameValue(name_value_dict)
            ],
            'id': comp_id
        })
    }
}


export default {NameValue, NameValueDisplayComponent};