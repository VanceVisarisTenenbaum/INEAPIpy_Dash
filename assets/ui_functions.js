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
    } else if (listOfINE_Objects === null){ return [];
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

function NewRowButtonComp(row_lv1=null){
    let name;
    if (row_lv1 === null){name = 'O';}
    else {name = 'VariableValor'}
    const boton = _html.Button({
        'children': 'Nueva fila',
        'n_clicks': 0,
        'id': id_generator_mapper(name, 'Boton', row_lv1),
        'className': 'Button'
    })
    const comp = _html.Div({
        'children': [boton],
        'className': 'ButtonContainer'
    })
    return comp;
}

function VarValPairBoxComponent(row_lv1, initial_vvp){
    const vvp = _html.Div({
        'children': [initial_vvp],
        'id': id_generator_mapper('VariableValor', 'Box', row_lv1),
        'className': 'RowSplitterBase RowSplitterSmall'
    })
    const comp = _html.Div({
        'children': [vvp, NewRowButtonComp(row_lv1)]
    })
}

function InputsGroupRow(row_lv1, op_comp, tab_comp, varvalbox_comp){
    const comp = _html.Div({
        'children': [
            op_comp,
            _html.Div({
                'children': [tab_comp, varvalbox_comp],
                'className': 'ColSplitterBase ColSplitterBig',
                'id': id_generator_mapper('TablaVVP', 'Box', row_lv1)
            })
        ],
        'id': id_generator_mapper('IG', None, row_lv1)
    })

    return comp;
}

function OperationSelectBox(row_lv1, requests_storage){
    const operaciones = extract_label_values(requests_storage['Operaciones']);
    const comp = SelectComponent(operaciones, 'O', row_lv1);
    return comp;
}

function TableSelectBox(row_lv1, tab_options){
    return SelectComponent(tab_options, 'T', row_lv1);
}

function make_vvp(row_lv1, row_lv2){
    const VrC = VariableComponent(row_lv1, row_lv2, variables);
    const VlC = ValorComponent(row_lv1, row_lv2, null);
    return VarValPair(VrC, VlC, row_lv1, row_lv2);
}

/* ------------------------------------------------------------------------- */

function get(obj, key, defaultValue = null) {
  return obj.hasOwnProperty(key) ? obj[key] : defaultValue;
}

/* ------------------------------------------------------------------------- */

function get_from_requests_storage(obj_typ, obj_depend, requests_storage){
    if (Number.isInteger(obj_depend)){throw new Error('obj_depend must be an integer.');}
    if (!['Variable', 'Valor', 'Tabla', 'Periodo'].includes(obj_type)){
        throw new Error('obj_type must be a valid value');
    }
    const data = get(get(requests_storage, obj_type), obj_depend, null);
    if (data === null){throw new Error('Data not found')}
    return data;
}


function make_var_val_comp(op_id, row_lv1, row_lv2, requests_storage){

    const variables = get_from_requests_storage('Variable', op_id, requests_storage);
    const VrC = VariableComponent(row_lv1, row_lv2, variables);
    const VlC = ValorComponent(row_lv1, row_lv2, null);
    return VarValPair(VrC, VlC, row_lv1, row_lv2);
}

function add_new_var_val_row(n_clicks, current_childrens, op_id, requests_storage){
    const patch = new dash_clientside.Patch;

    const row_lv1 = dash_clientside.callback_context.triggered_id['fila_lv1'];
    const row_lv2 = current_childrens.length + 1;
    const newVVP = make_var_val_comp(op_id,
                                   row_lv1, row_lv2 + 1,
                                   requests_storage);
    patch.append(newVVP);
    return patch
}

function add_options_to_input_value(dummy_storage, var_id, requests_storage){
    // dummy is just the input trigger, must be unique to this function
    const valores = extract_labels_values(requests_storage['Valor'][var_id]);
    return valores;
}

function add_options_to_input_table(dummy_storage, op_id, requests_storage){
    // dummy is just the input trigger, must be unique to this function
    const tablas = extract_labels_values(requests_storage['Tabla'][op_id]);
    return tablas;
}

function add_options_to_input_variable(dummy_storage, op_id, requests_storage){
    // dummy is just the input trigger, must be unique to this function
    const variable = extract_labels_values(requests_storage['Variable'][op_id]);
    return variable;
}

function add_new_op_row(n_clicks, current_childrens, requests_storage){
    console.log('Called');
    const patch = new dash_clientside.Patch;
    const row_lv1 = current_childrens.length + 1;
    const comp = InputsGroupRow(
        row_lv1,
        OperationSelectBox(row_lv1, requests_storage),
        TableSelectBox(row_lv1, []),
        VarValPairBoxComponent(
            row_lv1,
            make_vvp(row_lv1, 1)
        )
    );
    patch.append(comp);
    return patch;
}

/* ------------------------------------------------------------------------- */

window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'ui_functions': {
            'add_new_var_val_row': add_new_var_val_row,
            'add_options_to_input_value': add_options_to_input_value,
            'add_options_to_input_table': add_options_to_input_table,
            'add_options_to_input_variable': add_options_to_input_variable,
            'add_new_op_row': add_new_op_row
        }
    }
);
















