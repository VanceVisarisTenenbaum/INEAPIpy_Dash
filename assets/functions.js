/* Wrapper to create dash components at clientside.

   Example:

      _html.Div(
	    [_html.H4(["Hello World!", _dbc.Button("OK", {}, "btn_okay")],
                      {width: '100%', display: 'flex', justifyContent: 'space-between'}),
	     _dcc.Dropdown(null, {},
			   'cities',
			   {options: ['São Paulo', 'Rio de Janeiro'], value: 'São Paulo'}),
	     _dag.AgGrid(null, {},
      			 'grid_cities',
      			 {rowData: [{name: 'São Paulo', pop: 11.4},
				    {name: 'Rio de Janeiro', pop: 6.21}],
			  getRowStyle: {styleConditions: [{condition: 'params.data.name == "São Paulo"',
							   style: {backgroundColor: 'green',
								   fontWeight: 'bold',
								   color: 'white'
								  }}
							 ]},
      			  columnDefs: [{field: "name", headerName: 'City'},
				       {field: 'pop', headerName: 'Population (M)'}]
			 })
	    ]
	)


*/

const NAMESPACE_FROM_ACRONIM = {html: 'dash_html_components',
			 dcc: 'dash_core_components',
			 dbc: 'dash_bootstrap_components',
			 daq: 'dash_daq',
			 dag: 'dash_ag_grid',
			};

const new_dash_component = function(namespace_type,
			     children=[],
			     style={},
			     id='',
			     props={}) {
    const t = {};
    const [namespace, type] = namespace_type.split('.');
    t.namespace = NAMESPACE_FROM_ACRONIM[namespace];
    t.type = type;
    t.props = {children, style, id, ...props};
    return t;
}

const html_components = 'A Br Button Canvas Div H1 H2 H3 H4 H5 H6 Hr Link P Span Table Tbody Tr Th Td';
const dcc_components = 'Dropdown Graph Input Interval Link Slider Store Tab Tabs Textarea';
const daq_components = 'Slider';
const dbc_components = 'Button Checklist Input';
const dag_components = 'AgGrid';

window._html = {};
html_components.split(' ').map(
    comp => window._html[comp] = (...props) => new_dash_component(`html.${comp}`, ...props)
);

window._dcc = {};
dcc_components.split(' ').map(
    comp => window._dcc[comp] = (...props) => new_dash_component(`dcc.${comp}`, ...props)
);

window._daq = {};
daq_components.split(' ').map(
    comp => window._daq[comp] = (...props) => new_dash_component(`daq.${comp}`, ...props)
);

window._dbc = {};
dbc_components.split(' ').map(
    comp => window._dbc[comp] = (...props) => new_dash_component(`dbc.${comp}`, ...props)
);

window._dag = {};
dag_components.split(' ').map(
    comp => window._dag[comp] = (...props) => new_dash_component(`dag.${comp}`, ...props)
);

//console.log('Component functions are loaded')




// Custom components

const SELECT_INPUT_STYLE = {
    'width': '90%',
    'height': '100px',
    'fontSize': '15px'
}

function LabelInput(label, inputComp, style='top'){
    if (style === 'top'){
        return _html.Div({
            'children': [_html.Span(label), inputComp],
            'className': 'LabelInput LITop'
        });
    }
    else if (style === 'side'){
        return _html.Div({
            'children': [_html.Span(label), inputComp],
            'className': 'LabelInput LISide'
        });
    }
    else {
        throw new Error('style can only be side or top');
    }
    return null;
}


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
            let comp = _html.Div({
                'children': [
                    _html.Span(k, {'className': 'NameValName'}),
                    _html.Span(dict_value_process(v), {'className': 'NameValVal'})
                ],
                'className': 'NameValue'
            })
            childrens.push(comp);
        }
    );
    return _html.Div({
        'children': childrens,
        'className': 'NameValueGrid'
    });
}


function NameValueDisplayComponent(name_value_dict, comp_id, title=null){
    if (title === null){
        return _html.Div({
            'children': NameValue(name_value_dict),
            'id': comp_id
        })
    }
    else {
        return _html.Div({
            'children': [
                _html.H2(title),
                NameValue(name_value_dict)
            ],
            'id': comp_id
        })
    }
}


function id_generator(name, tipo=null, row_lv1=null, row_lv2=null){
    let = id_name = `type: ${name}`;
    if (tipo != null){id_name += `${tipo}`;}
    if (row_lv1 != null){
        let id_row1 = `fila_lv1: ${row_lv1}`;
        id_name += id_row1;
        if (row_lv2 != null){
            let id_row2 = `fila_lv2: ${row_lv2}`;
            id_name += id_row2;
        }
    }
    return id_name;
}

function name_mapper(short_name){
    map_dict = {
        'O': 'Operacion',
        'T': 'Tabla',
        'Vr': 'Variable',
        'Vl': 'Valor',
        'G': 'Grafica',
    }
    return map_dict[short_name] || short_name
}

function id_generator_mapper(name, tipo=null, row_lv1=null, row_lv2=null){
    return id_generator(name_mapper(name), tipo, row_lv1, row_lv2);
}


function extract_label_value(INE_object, onlyId = false) {
    if (typeof INE_object === 'object' && INE_object !== null) {
        if (onlyId) {
            return INE_object['Id'];
        }
        return { label: INE_object['Nombre'], value: INE_object['Id'] };
    } else {
        throw new Error('INE_object must be an object.');
    }
}

function extract_labels_values(listOfINE_Objects, onlyId = false) {
    if (Array.isArray(listOfINE_Objects)) {
        return listOfINE_Objects.map(x => extract_label_value(x, onlyId));
    } else if (typeof listOfINE_Objects === 'object' && listOfINE_Objects !== null) {
        return extract_label_value(listOfINE_Objects, onlyId);
    } else {
        throw new Error('list of INE object must be a list or object.');
    }
}

function SelectComponent(list_of_ine_obj, name, fila_lv1, fila_lv2=null, multi=False){
    let placeholder_v;
    if (multi){placeholder_v = 'Selecciona una o varias ' + name_mapper(name);}
    else {placeholder = 'Selecciona una '  + name_mapper(name);}

    let IC = _dcc.Dropdown({
        'options': extract_labels_values(list_of_ine_obj),
        'value': null,
        'id': id_generator_mapper(name, null, fila_lv1, fila_lv2),
        'style': SELECT_INPUT_STYLE,
        'multi': multi,
        'placeholder': placeholder_v
    });
    return LabelInput(name_mapper(name), IC);
}


function ValorComponent(row_lv1, row_lv2, list_of_ine_val){
    return SelectComponent(list_of_ine_val, 'Vl', row_lv1, row_lv2);
}

function VariableComponent(row_lv1, row_lv2, list_of_ine_var){
    return SelectComponent(list_of_ine_var, 'Vr', row_lv1, row_lv2);
}

function VarValPair(var_comp, val_comp, row_lv1, row_lv2){
    const Comp = _html.Div({
        'children':[var_comp, val_comp],
        'className': 'ColSplitterBase',
        'id': id_generator_mapper('VariableValor', None, row_lv1, row_lv2)
    });
    return Comp;
}



















