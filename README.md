# INEAPIpy Dash

Esta es una página web construida con dash encima del paquete [INEAPIpy](https://github.com/VanceVisarisTenenbaum/INEAPIpy).

La página permite navegar y utilizar la API del INE de una forma visual e intuitiva.

## Modo de empleo

1. Asegurarte de que estás en la carpeta correcta y de que has clonado el repositorio.
2. Instalar los requisitos: ```pip install requirements```.
3. Ejecutar la app ```python app.py```
4. Abrir la app en localhost, en la url indicada en la terminal.
* *Nota*: Si simplemente quieres aprovechar el layout hecho para dash, añade ```from Components.UIComponents.Main import initial_layout``` a tu código (o adapata la ruta), además de asegurar de cargar también la carpeta ```assets``` a tu app de dash.
