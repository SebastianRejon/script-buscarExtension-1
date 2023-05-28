# Mi script de Utilidad - Listado de Archivos "bak"
#### Este script nace de la necesidad que tengo como dibujante de recuperar u rastrear las distintos archivos de backUp de la Aplicacion Autodesk AutoCAD.
El programa de dibujo asistido por computadora "Auto CAD", manufacturado por Autodesk genera, durante la creacion de un archivo, uno o varios archivos con extension <<.bak>>; estos son puntos de restauracion automaticos que el soft gerera cada cierto tiempo. Cuando un archivo de CAD <<.dwg>> resulta corrupto o lo hemos cerrado sin guardar sus cambios es que podemos recurrir a este archivo de respaldo.

El script simplemente lista el contenido de todos los archivos que contengan la extesion <<.bak>>; ***esto con el fin de poder visualizar mas rapidamente su existencia. Se elije el metodo de listarlos uno debajo del otro por consola.***

Para la realizacion de este script he consultado las siguientes fuentes:
- https://markdown.es/
- https://docs.python.org/es/3.10/library/os.html
- http://www.tugurium.com/python/index.php?C=PYTHON.12_1_1
