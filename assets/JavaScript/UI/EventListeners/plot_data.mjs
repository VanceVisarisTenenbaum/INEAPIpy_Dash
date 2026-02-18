

// The function reads from requested data storage and plots the graphs.

import id_generator from '../Common/Functions/id_generator.mjs';
import ctx from '../Common/Functions/ctx_processing.mjs';
import get from '../Common/Functions/dictionary_processing.mjs';


function get_graph_data(childrens){
    const data_ = {

    };
    return data_
}

function row_process(row, index,
                    selected_graph_id,
                    selected_graph_val,
                    selected_graph_axis_id,
                    selected_graph_axis_val){
    if (index === 0){return null;}
    if (row['props']['data-checked'] === "0"){return null;}

    const id_ = row['props']['id']
    if (id_['Fila Nivel 1'] != selected_graph_id['Fila Nivel 1']){
        console.log(id_, selected_graph_id);
        throw new Error('Error 1, plot_data');
    }
    if (id_['Fila Nivel 1'] != selected_graph_axis_id['Fila Nivel 1']){
        console.log(id_, selected_graph_axis_id);
        throw new Error('Error 2, plot_data');
    }

    const data = {
        'serie_id': row['props']['data-serie-id'],
        'graph': selected_graph_val,
        'graph_axis': selected_graph_axis_val
    };
    return data;
}


function get_selected_series_data(table_childrens,
                                  graphs_ids, graphs_values,
                                  graphs_axis_ids, graphs_axis_values){
    let data_ = {};
    const lengths = [table_childrens.length-1, graphs_ids.length,  // -1 cause of header row
                     graphs_values.length, graphs_axis_ids.length,
                     graphs_axis_values.length]
    let all_equals = true;
    const first_val = lengths[0];
    for (let length of lengths){
        all_equals = all_equals && (length === first_val);
    }
    if (!all_equals){
        console.log(lengths);
        throw new Error('Some error I need to check in plot_data');
    }

    for (let i=1; i < table_childrens.length; i++){
        const row = table_childrens[i];
        const graph_id = graphs_ids[i-1];  // -1 por que el primer elemento de la lista es el 0, pero no para row, que 0 es el header
        const graph_val = graphs_values[i-1];
        const graph_axis_id = graphs_axis_ids[i-1];
        const graph_axis_val = graphs_axis_values[i-1];

        const row_data = row_process(row, i,
                                    graph_id, graph_val,
                                    graph_axis_id, graph_axis_val);
        if (row_data === null){continue;}
        data_[row_data['serie_id']] = {
            'Graph': row_data['graph'],
            'Graph_Axis': row_data['graph_axis']
        }
    }
    return data_;
}


function process_data(requested_serie_data, serie_cod, graph_axis){
    let axis;
    let mode;
    let type;
    if (graph_axis === 'Barras'){axis = 'y2'; type='bar'}
    else {axis = 'y'; mode='line+markers', type='scatter';}

    let x = [];
    let y = [];
    for (let data of requested_serie_data){
        x.push(new Date(data['Fecha']));
        y.push(data['Valor']);
    }
    const processed = {
        'x': x,
        'y': y,
        'name': serie_cod,
        'yaxis': 'y',
        'type': type,
    };
    return processed;
}

function make_layout(graph_id_num){
    const layout = {
        'title': 'Gráfica ' + String(graph_id_num),
        'showLegend': true
    }
    return layout;
}

function set_graph_data(graph_id_num, graph_data_list){


    let data_ = [];
    for (let i=0; i<graph_data_list.length; i++){
        let serie_data = graph_data_list[i]['data'];
        let serie_name = graph_data_list[i]['serie_cod'];
        let graph_axis = graph_data_list[i]['graph_axis'];
        data_.push(
            process_data(serie_data, serie_name, graph_axis)
        )
    }
    const figure_data = {
        'data': data_,
        'layout': {'title': make_layout(graph_id_num)}
    };
    const figure_id = id_generator(
        'Container', 'Grafica', 'Component', graph_id_num
    );
    dash_clientside.set_props(figure_id, {'figure': figure_data});
    return null;
}


function plot_graphs(
        requested_data,
        table_childrens,
        graphs_ids,
        graphs_values,
        graphs_axis_ids,
        graphs_axis_values
    ){

    // First we extract the selected graph and axis

    const selected_data = get_selected_series_data(
        table_childrens,
        graphs_ids, graphs_values,
        graphs_axis_ids, graphs_axis_values
    );

    if (Object.keys(selected_data).length != requested_data.length){
        throw new Error('Algún error, plot_graphs');
    }

    let figure_data = {};
    for (let serie_data of requested_data){
        let serie_cod = serie_data['COD'];
        let data = serie_data['Data'];
        let selected = selected_data[serie_cod];
        let graph = selected['Graph'];
        let graph_axis = selected['Graph_Axis'];
        console.log(serie_cod, data, selected);

        if (get(figure_data, graph, null) === null){
            figure_data[graph] = []
        }

        figure_data[graph].push(
            {
                'serie_cod': serie_cod,
                'graph_axis': graph_axis,
                'data': data
            }
        )
    }

    for (let graph_id_num of Object.keys(figure_data)){
        set_graph_data(parseInt(graph_id_num), figure_data[graph_id_num]);
    }

    return null;
}



window.dash_clientside = Object.assign(
    {},
    window.dash_clientside, {
        'plot_data': {
            'plot_graphs': plot_graphs,
        }
    }
);