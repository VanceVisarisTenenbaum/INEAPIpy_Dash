# Datos Abiertos INE (No Oficial)

Hola, este proyecto es un proyecto experimental, por lo que puede no funcionar correctamente.

El objetivo de la app es poder navegar y visualizar los datos proporcionados por la API del INE (Instituto Nacional de Estadísticas).

## Cómo se usa

El objetivo es seleccionar las series que quieres visualizar, pero para ello, primero es necesario filtrar las que quieres utilizando los filtros.
El proceso es el siguiente:

1. Seleccionas los filtros:
    1. Seleccionas al menos una Operación.
    2. Seleccionas al menos una Tabla o un par Variable Valor o ambos.
    * Puedes añadir pares variable valor utilizando el botón para añadir un nuevo par.
    * Puedes añadir operaciones utilizando el botón para añadir nuevo filtro.
2. Cierras la pestaña de filtros.
3. Cargas las series utilizando el botón arriba a la derecha, encima de la tabla.
4. Seleccionas las series:
    1. Click en la fila, aparece un contorno resaltando que ha sido seleccionada.
    2. Seleccionas la gráfica en la que quieres mostrar la serie.
    3. Seleccionas el tipo de gráfica que quiers mostrar, Línea o Barras.
    * La tabla está compuesta por cuatro columnas:
        * Operación: Indicando a qué operación pertenece la serie.
        * Serie: Nombre de la serie junto con el código identificador.
        * Selector de gráfica.
        * Selector de tipo de gráfica.
5. Cargas los datos utilizando el botón a la derecha, debajo de la tabla.
6. Se muestran los datos.


### Errores conocidos

Al ser un proyecto experimental, puede tener errores de diseño, algunos de estos son los siguientes:

* No hay feedback de si se están cargando los datos o no. Cuando seleccionas una Operación, se cargan las tablas y variables asociadas, y estas pueden tardar un poco en cargar, lo que significa que puede que no veas las tablas actualizadas al instante. Lo mismo ocurre con los valores al seleccionar una variable y al pulsar los botones para cargar las series y los datos.
* Al seleccionar una serie, esta se deselecciona al pinchar sobre la selección de gráfica y tipo de gráfica.
* Para abrir y cerrar la pestaña de los filtros, solo es posible utilizando el botón arriba a la izquierda.
