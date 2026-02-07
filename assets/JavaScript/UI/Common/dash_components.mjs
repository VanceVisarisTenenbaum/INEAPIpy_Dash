
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
			     //children=[],
			     //style={},
			     //id='',
			     props={}) {
    const t = {};
    const [namespace, type] = namespace_type.split('.');
    t.namespace = NAMESPACE_FROM_ACRONIM[namespace];
    t.type = type;
    //t.props = {children, style, id, ...props};
    t.props = {...props};
    return t;
}

const html_components = 'A Br Button Canvas Div H1 H2 H3 H4 H5 H6 Hr Link P Span Table Tbody Tr Th Td Header Section Summary Details';
const dcc_components = 'Dropdown Graph Input Interval Link Slider Store Tab Tabs Textarea RadioItems';
const daq_components = 'Slider';
const dbc_components = 'Button Checklist Input';
const dag_components = 'AgGrid';

let _html = {};
html_components.split(' ').map(
    comp => _html[comp] = (...props) => new_dash_component(`html.${comp}`, ...props)
);

let _dcc = {};
dcc_components.split(' ').map(
    comp => _dcc[comp] = (...props) => new_dash_component(`dcc.${comp}`, ...props)
);

let _daq = {};
daq_components.split(' ').map(
    comp => _daq[comp] = (...props) => new_dash_component(`daq.${comp}`, ...props)
);

let _dbc = {};
dbc_components.split(' ').map(
    comp => _dbc[comp] = (...props) => new_dash_component(`dbc.${comp}`, ...props)
);

let _dag = {};
dag_components.split(' ').map(
    comp => _dag[comp] = (...props) => new_dash_component(`dag.${comp}`, ...props)
);


export default {_html, _dcc, _daq, _dbc, _dag};